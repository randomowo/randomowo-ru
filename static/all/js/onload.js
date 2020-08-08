$(document).ready(function() {
    let api_pathname = document.getElementsByName("api-pathname")[0].value;
    let api_block_id = document.getElementsByName("block-id")[0].value;
    appendData(api_pathname, api_block_id);
});
