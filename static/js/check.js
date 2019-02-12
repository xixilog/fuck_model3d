function showUnreadNews() {
  $(document).ready(function() {
    $(".home").remove();
    $("#metaData").remove();
    $('a').remove();
  });
}


setInterval('showUnreadNews()', 100);
