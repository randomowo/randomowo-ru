getPage = () => {
    fetch("/admin/cinema/filmlist/", {
        method: "GET",
    })
        .then(response => location.reload(true));
}

validateForm = (form) => {
    for (let i=0; i < form.elements.length; i++) {
        const element = form.elements[i];
        if (element.required && element.value === "") {
            alert("Not valid form");
            element.focus();
            return false
        }
    }
    return true;
}

submitFilm = (form_id) => {
    const film_form = document.getElementById(form_id);
    let token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    data = {
        "csrfmiddlewaretoken": token,
    }
    if (!validateForm(film_form)) {
        return;
    }
    const film = {
        "id": film_form.elements[0].value,
        "title": film_form.elements[1].value,
        "url": film_form.elements[2].value,
        "director": film_form.elements[3].value,
        "year": film_form.elements[4].value,
        "is_watched": film_form.elements[5].checked,
        "is_movie": film_form.elements[6].checked,
        "seasons": []
    }
    if (!film["is_movie"]) {
        const film_form_list = film_form.querySelectorAll("fieldset");
        for (let i=0; i < film_form_list.length; i++) {
            const form = film_form_list[i];
            if (!validateForm(form)) {
                return;
            }
            if (form.id === "new-season") {
                film["seasons"].push({
                    "id": form.elements[0].value,
                    "number": form.elements[1].value,
                    "episodes": [],
                });
            } else if (form.id === "new-episode") {
                const episode = {
                    "id": form.elements[0].value,
                    "number": form.elements[1].value,
                    "title": form.elements[2].value,
                    "duration": form.elements[3].value,
                    "is_watched": form.elements[4].checked,
                }
                film["seasons"].slice(-1)[0]["episodes"].push(episode);
            }
        }
    }
    data["film"] = film;
    fetch("/admin/cinema/filmlist/", {
        method: "POST",
        headers: {
            "X-CSRFToken": token,
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data),
    })
        .then(response => {
            if (response.status === 400) {
                alert("Bad Request");
            } else {
                getPage();
            }
        });
}

removeFilm = (filmid, film_name) => {
    if (confirm(`Delete ${film_name}?`)) {
        let token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
        data = {
            "csrfmiddlewaretoken": token,
            "film_id": filmid,
        }
        fetch("/admin/cinema/filmlist/", {
            method: "DELETE",
            headers: {
                "X-CSRFToken": token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data),
        })
            .then(response => getPage());
    }
}


