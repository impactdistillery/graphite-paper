function handleVideo($ref, thumbURL, embedHTML) {
    $ref.append(thumbURL);

    $ref.on('click', function() {
        var $here = $(this);
        $here.html(embedHTML);
    });
}

function fetchTikTokData(video_id, $ref) {
    // Request TikTok oEmbed API for video information
    $.ajax({
        url: 'https://www.tiktok.com/oembed',
        data: {
            url: 'https://www.tiktok.com/@tiktok/video/' + video_id
        },
        success: function(response) {
            var thumb = '<i></i><img class="embed-responsive-item" src="' + response.thumbnail_url + '">';
            var embedHTML = response.html;

            handleVideo($ref, thumb, embedHTML);
        },
        error: function(error) {
            console.log("Error fetching TikTok data: ", error);
        }
    });
}

$(".youtube, .tiktok").each(function(index){
    var $ref = $(this);
    var video_id = $ref.attr("data-id");

    if ($ref.hasClass('youtube')) {
        // YouTube video handling
        var thumb = '<i></i><img class="embed-responsive-item" src="https://i.ytimg.com/vi/' + video_id + '/hqdefault.jpg">';
        var embedHTML = '<iframe class="embed-responsive-item" src="https://www.youtube-nocookie.com/embed/' + video_id + '?autoplay=1"></iframe>';

        handleVideo($ref, thumb, embedHTML);
    } else if ($ref.hasClass('tiktok')) {
        // TikTok video handling
        fetchTikTokData(video_id, $ref);
    }
});