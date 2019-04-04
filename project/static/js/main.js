
function setNextPrevArrows(){
  var mainContentHeight = parseInt($('#mainContent').height(), 10) + 'px';
  $('.nextPage div').css('line-height', mainContentHeight);
  $('.prevPage div').css('line-height', mainContentHeight);
}


responsiveVideos('only screen and (min-width: 768px) and (max-width: 1100px),only screen and (max-width: 480px),only screen and (min-width: 480px) and (max-width: 767px),only screen and (min-width: 1101px)');

$(document).ready(function(){

  if ($('.nextPage').length > 0 || $('.prevPage').length > 0) {
    setNextPrevArrows();
    $(window).resize(function(){
      setNextPrevArrows();
    });

    $(document).keydown( function(eventObject) {
      if($('.prevPage').length > 0){
        if(eventObject.which==37 || eventObject.which==75 || eventObject.which==72) {//left arrow, k and h
          window.location = $('.prevPage').attr('href');
        }
      }
      if($('.nextPage').length > 0) {
        if(eventObject.which==39 || eventObject.which==74 || eventObject.which==76) {//right arrow, j and l
          window.location = $('.nextPage').attr('href');
        }
      }
    });

  }

});
