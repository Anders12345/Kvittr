$(document).ready(function(){
    $(".add-likes-link").click(function(event) {
        event.preventDefault();
        var msg_id = $(this).data("msgid");
        $.ajax({
            url: $('#add_likes_url').val() + "/" + msg_id
        })
        .done(function(data){
            var likes_updated = data['likes_updated'];
            var likes_element_id = "#id-likes-for-msg-" + msg_id;
            $(likes_element_id).html(likes_updated);
        });
    });


 
});
