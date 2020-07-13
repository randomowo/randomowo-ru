addNewEl = (block_id, new_block) => {
    let block = document.getElementById(block_id);
    block.innerHTML += new_block;
}

let season_numb = 0;
addNewSeason = (block_id) => {
    season_numb++;
    let new_block = `
    <div class="film-season"
         id="film-season_${season_numb}">
            <div class="film-number">
                <input type="number"
                       id="film-season-number_${season_numb}"
                       name="film-season-number"
                       min="1"
                       required />
            </div>
            <div class="button"
                 id="button-season-remove">
                 <a onclick="removeEl('film-season_${season_numb}')">remove</a>
            </div>
        <div class="film-season-episode-block"
             id="film-season-episode-block_${season_numb}">
            <div class="button"
                 id="button-episode"
                 onclick="addNewEpisode('film-season-episode-block_${season_numb}', '${season_numb}')">
                <a href="#"> add episode </a>
            </div>
        </div>
    </div>`;

    addNewEl(block_id, new_block);
}

addNewEpisode = (block_id, sn) => {
    let new_block = `
    <div class="film-season-episode"
         id="film-season-episode_${sn}">
        <div class="film-number">
            <input type="number"
                id="film-episode-number_${sn}"
                name="film-episode-number_${sn}"
                placeholder="No."
                min="1"
                required />
        </div>
        <div class="film-text">
            <input type="text"
                id="film-episode-title_${sn}"
                name="film-episode-title_${sn}"
                placeholder="Episode title" />
        </div>
        <div class="film-number">
            <input type="number"
                id="film-episode-duration_${sn}"
                name="film-episode-duration_${sn}"
                placeholder="Duration" />
    </div>`;


    addNewEl(block_id, new_block);
}

removeEl = (block_id) => {
    document.getElementById(block_id).remove();
}
