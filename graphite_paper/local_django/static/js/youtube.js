console.log("YOUTUBE")

$(".youtube").each(function(index){
    var $ref = $(this)
    var video_id = $ref.attr("data-id")
    var thumb = '<i></i><img class="embed-responsive-item" src="https://i.ytimg.com/vi/' + video_id + '/hqdefault.jpg">'
    console.log(thumb)
    $ref.append(thumb)
    $ref.click(function(){
        var $here = $(this)
        video_id = $here.attr("data-id")
        console.log(video_id)
        console.log($here)
        var myiframe = '<iframe class="embed-responsive-item" src="https://www.youtube.com/embed/' + video_id + '?autoplay=1"></iframe>'
        $here.html(myiframe)
    })
})
