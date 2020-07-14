submitFilm = (form_id) => {
    const film_form = document.getElementById(form_id);
    let token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    data = {
        "csrfmiddlewaretoken": token,
    }
    const film = {
        "title": film_form.elements[0].value,
        "url": film_form.elements[1].value,
        "director": film_form.elements[2].value,
        "year": film_form.elements[3].value,
        "is_watched": film_form.elements[4].checked,
        "is_movie": film_form.elements[5].checked,
        "seasons": []
    }
    if (!film["is_movie"]) {
        const film_form_list = film_form.querySelectorAll("fieldset");
        for (let i=0; i < film_form_list.length; i++) {
            const form = film_form_list[i];
            if (form.id === "new-season") {
                film["seasons"].push({
                    "number": form.elements[0].value,
                    "episodes": [],
                });
            } else if (form.id === "new-episode") {
                const episode = {
                    "number": form.elements[0].value,
                    "title": form.elements[1].value,
                    "duration": form.elements[2].value,
                    "is_watched": form.elements[3].checked,
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
        .then(response => response.json())
        .then(location.reload());

}
