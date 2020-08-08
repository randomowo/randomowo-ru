toggleCheckbox = (block, type, season_block_id) => {
    const checkbox = document.getElementsByName(block)[0];
    checkbox.checked = !checkbox.checked;
    if (season_block_id !== "") $(`#${season_block_id}`).toggle(!checkbox.checked);
    if (checkbox.checked) {
        $(`#${block}`).addClass(type+"-checked-box");
    } else {
        $(`#${block}`).removeClass(type+"-checked-box");
    }
}
