toggle = (id, id2, name) => {
    const n = document.getElementById(id);
    const el = document.getElementById(id2);
    if (n.style.display != 'none') {
        n.style.display = 'none';
        el.setAttribute('aria-expanded', 'false');
        el.textContent = name;
        el.classList.remove("expanded-button")
    } else {
        n.style.display = '';
        el.setAttribute('aria-expanded', 'true');
        el.textContent = "^";
        el.classList.add("expanded-button")
    }
}
