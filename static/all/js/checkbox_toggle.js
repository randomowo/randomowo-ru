checkebox_toggle = (id, block_id) => {
    $(`#${id}`).click(function() {
        $(`#${block_id}`).toggle(!this.checked);
    });
}
