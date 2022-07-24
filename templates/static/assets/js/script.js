
const addIemForm = ".add-item-form";

$(document).on("submit", addIemForm, function (event) {
    event.preventDefault();
    console.log("kock");
    var data = $(addIemForm).serialize()
    console.log(data);
    $.ajax({
        url: "/inventory/add-item/",
        type: "POST",
        headers: { "X-CSRFToken": csrftoken },
        data: data,
        success: function(response) {
            console.log(response);
            console.log("Added!");
            alert("Added!");
        },
        complete: function() {
        }
    });
});