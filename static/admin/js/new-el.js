let season_numb = 0;
addNewSeason = (block_id, is_new) => {
    season_numb++;
    is_new = is_new === '' ? '' : "-"+is_new;
    let new_block = `
    <div class="film-season"
         id="film-season${is_new}_${season_numb}">
        <fieldset id="new-season">
             <div class="button"
                  id="button-season-remove"
                  onclick="removeEl('film-season${is_new}_${season_numb}', 'new-season')">
                  remove
             </div>
             <input type="hidden"
                    id="film-season-id"
                    name="film-season-id"
                    value="" />
             <div class="season-field-block">
                <div class="season-label">
                    Season No.
                </div>
                <div class="season-field">
                    <input type="number"
                           id="film-season-number${is_new}_${season_numb}"
                           name="film-season-number"
                           min="1"
                           placeholder="No."
                           required />
                </div>
            </div>
            <div class="film-season-episode-block"
                 id="film-season-episode-block${is_new}_${season_numb}">
                <div class="button"
                     id="button-episode"
                     onclick="addNewEpisode('film-season-episode-block${is_new}_${season_numb}', '${is_new}')">
                    add episode
                </div>
            </div>
        </filedset>
    </div>
`;

    $(`#${block_id}`).append(new_block);
}

let episode_numb = 0;
addNewEpisode = (block_id, is_new) => {
    episode_numb++;
    is_new = is_new === '' ? '' : is_new;
    let new_block = `
    <div class=film-season-episode"
         id="film-season-episode${is_new}_${episode_numb}">
        <fieldset id="new-episode">
            <div class="episode-element">
                <div class="button remove-button"
                     onclick="removeEl('film-season-episode${is_new}_${episode_numb}', 'new-episode')">
                     remove
                </div>
            </div>
            <input type="hidden"
                   id="film-season-episode-id${is_new}"
                   name="film-season-episode-id"
                   value="" />
            <div class="episode-field-block">
                 <div class="episode-label">
                     Episode No.
                 </div>
                <div class="episode-field">
                    <input type="number"
                        id="film-episode-number${is_new}"
                        name="film-episode-number"
                        placeholder="No."
                        min="1"
                        required />
                </div>
            </div>
            <div class="episode-field-block">
                 <div class="episode-label">
                     Episode title
                 </div>
                <div class="episode-field">
                    <input type="text"
                        id="film-episode-title${is_new}"
                        name="film-episode-title"
                        placeholder="Episode title" />
                </div>
            </div>
            <div class="episode-field-block">
                 <div class="episode-label">
                     Episode duration (minutes)
                 </div>
                <div class="episode-field">
                    <input type="number"
                        id="film-episode-duration${is_new}"
                        name="film-episode-duration"
                        placeholder="Duration" />
                </div>
            </div>
            <div class="episode-element">
            <div class="episode-checkbox"
                 id="film-episode-is-watched${is_new}_${episode_numb}"
                 onclick="toggleCheckbox('film-episode-is-watched${is_new}_${episode_numb}', 'episode', '')">
                     Episode is watched
                 </div>
                 <input type="checkbox"
                        name="film-episode-is-watched${is_new}_${episode_numb}" />
            </div>
            
        </fieldset>
    </div>
`;

    $(`#${block_id}`).append(new_block);
}

removeEl = (block_id) => {
    $(`#${block_id}`).remove();
}
