var LFTF = LFTF || {};

LFTF.init = function() {
    var autoplay = window.location.search.substring(1),
        youTubeFrame = $('iframe.band_video');

    if (autoplay === 'autoplay') {
        youTubeFrame.attr('src', LFTF.iframeSrc);
        $('.featured a').css("display", "none");
    }

    $('.band_page .featured a').click(function() {
        event.preventDefault();
        $(this).fadeOut(600);
        youTubeFrame.attr('src', LFTF.iframeSrc);
    });

};

LFTF.init();
