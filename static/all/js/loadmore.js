$(window).scroll(function() {
    if($(window).scrollTop() == $(document).height() - $(window).height()) {
        let api_pathname = document.getElementsByName("api-pathname")[0].value;
        let api_block_id = document.getElementsByName("block-id")[0].value;
        appendData(api_pathname, api_block_id);
    }
});

appendData = (url, block) => {
    let start = Number(document.getElementsByName("count")[0].value);
    let count = 30;
    let uri = url+"?count="+count+"&start="+start;
    $.ajax({
        url: uri,
        contentType: "application/json",
        cache: false,
        success: response => {
            data = JSON.parse(response);
            if (data.length > 0) {
                addAdminFilm(data, block);
                document.getElementsByName("count")[0].setAttribute("value", start+count);
            }
        }
    });
}

addAdminFilm = (data, block) => {
    data.forEach(film => {
        $(`#${block}`).append(getFilmBlock(film));
    });
}

getFilmBlock = (film) => {
    let block = `
    <div id="film-block"
                 class="film-block">
                <div class="button"
                     id="button-film${film["id"]}"
                     onclick="toggle('film-content${film["id"]}', 'button-film${film["id"]}', '${film["title"]}')">
                    ${film["title"]}
                </div>
                <div class="film-content"
                     id="film-content${film["id"]}"
                     style="display:none">
                    <form id="film-update-form${film["id"]}">
                        <div class="film-element">
                            <div class="button"
                                 id="button-remove-film"
                                 onclick="removeFilm('${film["id"]}')">
                                remove
                            </div>
                        </div>
                        <input type="hidden"
                               id="film-id"
                               name="film-id"
                               value="${film["id"]}" />
                        <div class="film-field-block">
                            <div class="film-label">
                                Title
                            </div>
                            <div class="film-field">
                                <input type="text"
                                       id="film-title"
                                       name="film-title"
                                       placeholder="Title"
                                       value="${film["title"]}"
                                       required />
                            </div>
                        </div>
                        <div class="film-field-block">
                            <div class="film-label">
                                URL
                            </div>
                            <div class="film-field">
                                <input type="text"
                                       id="film-url"
                                       name="film-url"
                                       placeholder="Url to film page"
                                       value="${film["url"]}"
                                       required />
                            </div>
                        </div>
                        <div class="film-field-block">
                            <div class="film-label">
                                Director
                            </div>
                            <div class="film-field">
                                <input type="text"
                                       id="film-director"
                                       name="film-director"
                                       placeholder="Director"
                                       value="${film["director"]}"
                                       required />
                            </div>
                        </div>
                        <div class="film-field-block">
                            <div class="film-label">
                                Year
                            </div>
                            <div class="film-field">
                                <input type="number"
                                       id="film-year"
                                       name="film-year"
                                       placeholder="Year"
                                       min="1900"
                                       max="${new Date().getFullYear() + 1}"
                                       step="1"
                                       value="${film["year"]}"
                                       required />
                            </div>
                        </div>
                        <div class="film-element">
                            <div class="film-checkbox ${ film["is_watched"] ? "film-checked-box" : "" }"
                                id="film-is-watched${film["id"]}"
                                onclick="toggleCheckbox('film-is-watched${film["id"]}', 'film', '')">
                                    Is watched?
                                </div>
                                <input type="checkbox"
                                       name="film-is-watched${film["id"]}"
                                       ${ film["is_watched"] ? "checked" : "" } />
                            <div class="film-checkbox ${ film["is_movie"] ? "film-checked-box" : "" }"
                                id="film-is-movie${film["id"]}"
                                onclick="toggleCheckbox('film-is-movie${film["id"]}', 'film', 'film-season-block${film["id"]}')">
                                    Is a movie?
                                </div>
                                <input type="checkbox"
                                       name="film-is-movie${film["id"]}"
                                       ${ film["is_movie"] ? "checked" : "" } />
                        </div>
                        <div class="film-element">
                            <div class="film-season-block"
                                 id="film-season-block${film["id"]}"
                                 ${ film["is_movie"] ? "style=\"display:none\"" : "" }>
                                <div class="button"
                                     id="button-season"
                                     onclick="addNewSeason('film-season-block${film["id"]}', '')">
                                    add season
                                </div>
                            `;
    film["seasons"].forEach( season => {
        block += `
        <div class="film-season"
         id="film-season_${season["id"]}">
        <fieldset id="new-season">
            <div class="button"
                 id="button-season-remove"
                 onclick="removeEl('film-season_${season["id"]}')">
                remove
            </div>
            <input type="hidden"
                   id="film-season-id"
                   name="film-season.id"
                   value="${season["id"]}" />
            <div class="season-field-block">
                <div class="season-label">
                    Season No.
                </div>
                <div class="season-field">
                    <input type="number"
                           id="film-season-number"
                           name="film-season-number"
                           min="1"
                           placeholder="No."
                           value="${season["number"]}"
                           required />
                </div>
            </div>
            <div class="film-season-episode-block"
                 id="film-season-episode-block_${season["id"]}">
                <div class="button"
                     id="button-episode"
                     onclick="addNewEpisode('film-season-episode-block_${season["id"]}',
                     '${season["id"]}', '')">
                    add episode
                </div>

        `;
        season["episodes"].forEach( episode => {
            block += `
            <div class=film-season-episode"
                 id="film-season-episode_${episode["id"]}">
                <fieldset id="new-episode">
                    <div class="button"
                         id="button-episode-remove"
                         onclick="removeEl('film-season-episode_${episode["id"]}')">
                        remove
                    </div>
                    <input type="hidden"
                           id="film-season-episode-id"
                           name="film-season-episode-id"
                           value="${episode["id"]}" />
                    <div class="episode-field-block">
                        <div class="episode-label">
                            Episode No.
                        </div>
                        <div class="episode-field">
                            <input type="number"
                                   id="film-episode-number"
                                   name="film-episode-number"
                                   placeholder="No."
                                   min="1"
                                   value="${episode["number"]}"
                                   required />
                        </div>
                    </div>
                    <div class="episode-field-block">
                        <div class="episode-label">
                            Episode title
                        </div>
                        <div class="episode-field">
                            <input type="text"
                                   id="film-episode-title"
                                   name="film-episode-title"
                                   placeholder="Episode title"
                                   value="${episode["title"]}" />
                        </div>
                    </div>
                    <div class="episode-field-block">
                        <div class="episode-label">
                            Episode duration (minutes)
                        </div>
                        <div class="episode-field">
                            <input type="number"
                                   id="film-episode-duration"
                                   name="film-episode-duration"
                                   placeholder="Duration"
                                   value="${episode["duration"]}" />
                        </div>
                    </div>
                    <div class="episode-element">
                        <div class="episode-checkbox ${episode["is_watched"] ? "episode-checked-box" : ""}"
                             id="film-episode-is-watched${episode["id"]}"
                             onclick="toggleCheckbox('film-episode-is-watched${episode["id"]}', 'episode', '')">
                                Episode is watched
                            </div>
                            <input type="checkbox"
                                   name="film-episode-is-watched${episode["id"]}"
                                   ${episode["is_watched"] ? "checked" : ""} />
                    </div>
                </fieldset>
            </div>
            `;
        });
        block += "</div></fieldset>";
    });
    block += `
                    </div>
                        </div>
                        <div class="film-element">
                            <div class="button add-button"
                                 onclick="submitFilm('film-update-form${film["id"]}')">
                                update
                            </div>
                        </div>
                    </form>
                </div>
            </div>`;

    return block;
}
