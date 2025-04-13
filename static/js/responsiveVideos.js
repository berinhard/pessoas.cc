
/*

  responsiveVideos.js, v0.2.0.

  Author: Luciano Ratamero
  Released under the MIT License

  https://github.com/lucianoratamero/responsiveVideos.js

*/

(function() {

  this.responsiveVideos = function(mediaQueries){

    var mediaQueriesList = mediaQueries.split(',');
    var embeddedVideosList = document.getElementsByClassName('embeddedVideo');
    var embeddedVideosListLength = document.getElementsByClassName('embeddedVideo').length;

    function calculateVideoSize(){

      for (var i=0; i<embeddedVideosListLength; i++) {

        var embeddedVideoMaxWidth,
            embeddedVideoMaxHeight,
            embeddedVideoMinWidth,
            el = embeddedVideosList[i],
            container = el.parentNode,
            video = el.getElementsByTagName('iframe')[0];

        if (el.getAttribute('data-max-width')) {
          embeddedVideoMaxWidth = el.getAttribute('data-max-width');
        } else {
          embeddedVideoMaxWidth = '560';
        }

        if (el.getAttribute('data-max-height')) {
          embeddedVideoMaxHeight = el.getAttribute('data-max-height');
        } else {
          embeddedVideoMaxHeight = parseInt(embeddedVideoMaxWidth) * 0.5625; // youtube's default aspect ratio
        }

        if (el.getAttribute('data-min-width')) {
          embeddedVideoMinWidth = el.getAttribute('data-min-width');
        } else {
          embeddedVideoMinWidth = '300'; // max-width of smallest smart devices
        }

        var customAspectRatio = parseInt(embeddedVideoMaxHeight)/parseInt(embeddedVideoMaxWidth);

        video.setAttribute('width', embeddedVideoMaxWidth||'560')   // youtube's default embedded width
        video.setAttribute('height', embeddedVideoMaxHeight||'315') // youtube's default embedded height

        if (parseInt(container.offsetWidth) > embeddedVideoMaxWidth) {
          // default case
          video.setAttribute('width', embeddedVideoMaxWidth||'560')   // youtube's default embedded width
          video.setAttribute('height', embeddedVideoMaxHeight||'315') // youtube's default embedded height
        } else if (parseInt(container.offsetWidth) < video.getAttribute('width')) {
          // cases for when window becomes smaller
          if (parseInt(container.offsetWidth) > embeddedVideoMinWidth){
            video.setAttribute('width', parseInt(container.offsetWidth))
            video.setAttribute('height', parseInt(container.offsetWidth) * customAspectRatio)
          } else if (parseInt(container.offsetWidth) <= embeddedVideoMinWidth) {
            video.setAttribute('width', embeddedVideoMinWidth)
            video.setAttribute('height', embeddedVideoMinWidth * customAspectRatio)
          }

        }

      }

    }

    mediaQueriesList.forEach(function(mediaQuery){
      Harvey.attach(mediaQuery, {
        on: function(){calculateVideoSize();}, // called each time the query is activated
      });
    });

  }

}).call(this);
