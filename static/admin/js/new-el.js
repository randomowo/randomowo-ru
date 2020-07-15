let season_numb = 0;
addNewSeason = (block_id, is_new) => {
    season_numb++;
    is_new = is_new === '' ? '' : "-"+is_new;
    let new_block = `
    <div class="film-season"
         id="film-season${is_new}_${season_numb}">
        <fieldset id="new-season">
             <input type="hidden"
                    id="film-season-id"
                    name="film-season-id"
                    value="" />
             <div class="season-element">
                <div class="season-label">
                    Season No.
                </div>
                <div class="film-number">
                    <input type="number"
                           id="film-season-number${is_new}_${season_numb}"
                           name="film-season-number"
                           min="1"
                           placeholder="No."
                           required />
                </div>
            </div>
            <div class="button"
                 id="button-season-remove"
                 onclick="removeEl('film-season${is_new}_${season_numb}')">
                 remove
            </div>
            <div class="film-season-episode-block"
                 id="film-season-episode-block${is_new}_${season_numb}">
                <div class="button"
                     id="button-episode"
                     onclick="addNewEpisode('film-season-episode-block${is_new}_${season_numb}', '${season_numb}', 'new')">
                    add episode
                </div>
            </div>
        </filedset>
    </div>
`;

    $(`#${block_id}`).append(new_block);
}

addNewEpisode = (block_id, sn, is_new) => {
    is_new = is_new === '' ? '' : "-"+is_new;
    let new_block = `
    <div class=film-season-episode"
         id="film-season-episode${is_new}">
        <fieldset id="new-episode">
            <input type="hidden"
                   id="film-season-episode-id${is_new}"
                   name="film-season-episode-id"
                   value="" />
            <div class="episode-element">
                 <div class="episode-label">
                     Episode No.
                 </div>
                <div class="film-number">
                    <input type="number"
                        id="film-episode-number${is_new}"
                        name="film-episode-number"
                        placeholder="No."
                        min="1"
                        required />
                </div>
            </div>
            <div class="episode-element">
                 <div class="episode-label">
                     Episode title
                 </div>
                <div class="film-text">
                    <input type="text"
                        id="film-episode-title${is_new}"
                        name="film-episode-title"
                        placeholder="Episode title" />
                </div>
            </div>
            <div class="episode-element">
                 <div class="episode-label">
                     Episode duration (minutes)
                 </div>
                <div class="film-number">
                    <input type="number"
                        id="film-episode-duration${is_new}"
                        name="film-episode-duration"
                        placeholder="Duration" />
                </div>
            </div>
            <div class="episode-element">
                 <div class="episode-label">
                     Episode is_watched
                 </div>
                 <div class="film-checkbox">
                    <input type="checkbox"
                           id="film-episode-is-watched${is_new}"
                           name="film-episode-is-watched" />
                 </div>
            </div>
        </fieldset>
    </div>
`;

    $(`#${block_id}`).append(new_block);
}

removeEl = (block_id) => {
    $(`#${block_id}`).remove();
}
