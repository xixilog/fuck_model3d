function showUnreadNews() {
  var home = jQuery('.home');

  if (home.length > 0) {

    $(".home").parent().prepend("<div onclick='change()'><center><i id='audio_state' class='fa fa-play-circle' aria-hidden='true'></i></center></div>")

    $(".home").remove();

    var audio = $("#the_audio")[0];
    audio.play();

  }


  var metaData = jQuery('#metaData');

  if (metaData.length > 0) {

    $("#metaData").remove();

  }

  var tag_a = jQuery('a');

  if (tag_a.length > 0) {

    $('a').remove();

  }

  var myAudio = document.getElementById('the_audio');

  if (myAudio.paused) {
    document.getElementById('audio_state').className = "fa fa-pause-circle";
  } else {
    document.getElementById('audio_state').className = "fa fa-play-circle";
  }

}


setInterval('showUnreadNews()', 100);


function change() {
  Play = document.getElementById("the_audio");
  if (document.getElementById('audio_state').className == "fa fa-play-circle") {
    Play.pause();
    document.getElementById('audio_state').className = "fa fa-pause-circle";
  } else {
    Play.play();
    document.getElementById('audio_state').className = "fa fa-play-circle";
  }
}
