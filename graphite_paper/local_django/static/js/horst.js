/*jslint browser: true*/
/*global $, jQuery, alert, console*/


// ToggleText function
$.fn.extend({
    toggleText: function(a, b){
        return this.text(this.text() == b ? a : b);
    }
});

//
// Normalise slide height to prevent jumping
//---------------------------------------------------------
function normaliseSlidesHeight(){
    var $slides = $(".slides-norm-height");
    $slides.each(function (index) {
//        console.log(index);
//        console.log($slides[index].id);
        carouselNormalization($slides[index].id);
    });
}

function carouselNormalization(carousel_id) {
//var items = $('#579carouselExampleIndicators .carousel-item'), //grab all slides
    var target = '#' + carousel_id + ' .carousel-item .ms-row';
    console.log(target);
    var items = $(target), //grab all slides
        heights = [], //create empty array to store height values
        tallest; //create variable to make note of the tallest slide

    if (items.length) {

        normalizeHeights(items, heights, tallest);

        $(window).on('resize orientationchange', function () {
            tallest = 0;
            heights.length = 0; //reset vars
            items.each(function () {
                $(this).css('min-height', '0'); //reset min-height
            });
            normalizeHeights(items, heights, tallest); //run it again
        });
    }
}

function normalizeHeights(items, heights, tallest) {
    items.each(function () { //add heights to array
        heights.push($(this).actual('height'));
    });
    tallest = Math.max.apply(null, heights); //cache largest value
    console.log(heights);
    console.log("Tallest: "  + tallest);
    items.each(function () {
        $(this).css('min-height', (tallest) + 'px');
        $(this).parent().parent().css("height", (tallest + 50) + "px");
        $(this).parent().parent().css("overflow-y", "hidden");
        console.log($(this));
    });
}


//
// Table of contents
//-----------------------------------------------------------------
var selector;

function makeToC() {
    console.log('Creating TOC …')
    $('article').attr('data-spy', 'scroll');
    $('body').attr('data-target', '.ms-toc');
    $('article').attr('data-offset', '-300');

    $('.ms-toc').empty();
    $('.ms-toc').append('<ul class="ms-toc-entries nav nav-pills  sticky-top flex-column side-nav" aria-hidden="false"></ul>').append('<ul class="ms-toc-abstract-entries nav nav-pills  sticky-top flex-column side-nav" aria-hidden="true"></ul>');

    selector = $('.tab-pane.active article :header');

    addReduced();
    addDetailed();

    enableListener();
    console.log('TOC refreshed')
}

// Build abstract lines
function addReduced() {
    // foreach header append a line
    for (var i = 0; i < selector.length; i++) {

        if ($(selector[i]).attr('id')) {
            // Add elements to nav
            for (var j=2; j < 5; j++){
                if (selector[i].nodeName == 'H'+j) {
                    $('ul.ms-toc-abstract-entries').append('<li class="nav-item side-nav ms-toc-abstract-entry ms-toc-abstract-entry ms-toc-abstract-entry-' + j + '"><a class="nav-link side-nav ms-toc-entry-link" href="#' + $(selector[i]).attr('id') + '"></a></li>')
                }
            }
        }
    }
}

// Build full toc
function addDetailed() {
    // foreach header append a line
    for (var i = 0; i < selector.length; i++) {

        if ($(selector[i]).attr('id')) {
            // Add elements to nav
            for (var j=0; j < 4; j++){
                if (selector[i].nodeName == 'H'+j) {
                    $('ul.ms-toc-entries').append('<li class="nav-item side-nav ms-toc-entry ms-toc-entry-level' + j + '"><a class="nav-link side-nav ms-toc-entry-link" href="#' + $(selector[i]).attr('id') + '">' + selector[i].textContent + '</a></li>')
                }
            }
        }
    }
}

//
// Collapse oversized marginal notes
//-------------------------------------------------------------
function collapseOversizedMarginals() {
    $('.tab-pane.active .ms-text').each(function () {
        var numAsides = $(this).children('.ms-col-marginal').children('aside').length;

        /* Deal with marginals if exist */
        if (numAsides>0) {

            var isOverflowing = false;
            var canOverflow = false;

            /* Content heights */
            var heightAsides = 0;
            $(this).children('.ms-col-marginal').children('aside').each(function () {
                heightAsides = heightAsides + $(this).height();
            });
//                console.log('Asides:', $(this), heightAsides)
            var heightContent = $(this).children('.ms-col-content').children('p').height();
//                console.log('Content:', $(this), heightContent)

            /* Check whitespace under content */
            if (heightAsides - heightContent > 20){
                isOverflowing = true;
            }

            /* Check if there is no asides or plugins after overflowing, single aside */
            // TODO, check hight of next element, let all children flow?
            if ($(this).next().hasClass('ms-text')){
                if ($(this).next().children('.ms-col-marginal').children().length == 0) {
                    if (numAsides < 2){
                        canOverflow = true;
                        }
                }
            }

            if (isOverflowing) {
                // if overflow possible, just set height of row
                if (canOverflow) {
                    $(this).children('.ms-col-marginal').addClass('marginals-overflowing');
                    $(this).children('.ms-col-marginal').css('max-height', heightContent);
                    $(this).children('.ms-col-marginal').children('aside').addClass('show');
                }
                // otherwise start collapsing
                else {

                    // set hight of marginal to be no more than content
                    $(this).children('.ms-col-marginal').addClass('marginals-collapsed');
                    $(this).children('.ms-col-marginal').css('max-height', heightContent);

                    /* Calculate aside height */
                    numAsides = $(this).children('.ms-col-marginal').children(' aside').length;

                    var medHeightAsides = (heightContent) / numAsides;
                    medHeightAsides = medHeightAsides - 10;

                    $(this).children('.ms-col-marginal').children(' aside').each(function() {
                        if ($(this).children('p').height() < medHeightAsides) {
                            $(this).css('flex-shrink', 0);
                            $(this).css('flex-grow', 0);
                            $(this).css('flex-basis', $(this).children('p').height());
                            $(this).addClass('show');
                        }
                        else{
                            $(this).css('flex-shrink', 1);
                            $(this).css('flex-basis', medHeightAsides);
                            $(this).addClass('collapsed');
                        }
                    });

    //                $(this).children('.ms-col-marginal').children(' aside').css('height', heightAsides);
                }

            }
            else{
                $(this).children('.ms-col-marginal').children('aside').addClass('show');
            }

        }


    });
}

//
// Collapse oversized infobox
//-------------------------------------------------------------
function collapseOversizedInfobox() {
    $('.ms-plugin-infobox').each(function () {

        var isOverflowing = false;
        var canOverflow = false;
        var maxHeight = 200;

        /* Check height */
        var heightContent = $(this).height();
        if (heightContent > maxHeight){
            isOverflowing = true;
        }

        /* Check if there is no asides or plugins after overflowing, single aside */
        // TODO, check hight of next element, let all children flow?
        if ($(this).hasClass('collapse')){
            canOverflow = true;
        }

        if (isOverflowing) {
            // if overflow possible, just set height of row
            if (canOverflow) {
                $(this).addClass('infobox-overflowing');
//                $(this).css('max-height', maxHeight);
            }
            $(this).after('<button class="btn btn-primary toggleInfobox" type="button">Expand infobox</button>')

            enableListener();
        }
    });
}


//
// Handle anchor links
//-------------------------------------------------------------



function handleAnchorLinks(hashValue) {
    var offset = 80;

    if($(hashValue).hasClass('tab-pane')){
        console.log('Clicked a tab')

        // Show tab
        // (bootstraps throws error, used try catch to continue script)
        try {
            $("a[href='"+hashValue+"']").tab('show');
        } catch(err) {
            console.log('Changing tab errors: ', err)
        }

        //Reload TOC and collapse/show marginals after changing tabs
//            console.log('Calling makeToC from handleAnchorLinks TAB')
        setTimeout(makeToC, 200);
        setTimeout(collapseOversizedMarginals, 300);

        // Scroll to top if below fixed tabs
        if ($('.ms-tabs')[0].getBoundingClientRect().top === 0){
            var firstElementClass = hashValue + ' .ms-row:first-child'
            setTimeout(function(){
                $(firstElementClass)[0].scrollIntoView(true)
                scrollBy(0, -offset);
            },
            200);
        }

    }
    else if(hashValue.includes('heading')){
        console.log('Clicked a heading')

        var tabID = '#'+$(hashValue).parents('.tab-pane').attr('id')
//        console.log('tab id', tabID )

        try {
            $("a[href='"+tabID+"']").tab('show');
        } catch(err) {
            console.log('Changing tab errors: ', err)
        }
//        console.log('Calling makeToC from handleAnchorLinks HEADING')
        setTimeout(makeToC, 200);

        setTimeout(function(){
            $(hashValue)[0].scrollIntoView(true);
            scrollBy(0, -offset);
        },
        200);

    }
    else{
        console.log('hash unknown')
    }

    window.location.hash = hashValue;
}

//
// Event listener
//---------------------------------------------------------------


function enableListener() {

    // Tab-button on mobile
    $(".tab-item").click(function(value) {
        $("#dropdownMenuButton").text($(this).text());
    });

    // Pause Carousel
    $('.carousel-item .ms-col-content').click(function(){


        if ($(this).parents('.carousel').hasClass('paused')) {
            $(this).parents('.carousel-item').addClass('play').delay(800).queue(function() {
                $(this).removeClass('play').dequeue();
            });
            $(this).parents('.carousel').toggleClass('paused');
            $(this).parents('.carousel').carousel('cycle');
            $(this).parents('.carousel').delay(500).queue(function() {
                $(this).carousel('next').dequeue();
            });
        }
        else{
            $(this).parents('.carousel-item').addClass('pause').delay(800).queue(function(){
                $(this).removeClass('pause').dequeue();
            });
            $(this).parents('.carousel').toggleClass('paused');
            $(this).parents('.carousel').carousel('pause');
        }


    });

    // Show collapsed marginals on click
    $('.marginals-collapsed').children('aside').unbind('click').click(function () {
        $(this).toggleClass('show-collapsed');
    });

    $('.marginals-collapsed').children('aside').mouseleave(function () {
        $(this).removeClass('show-collapsed');
    });

    // Toggle infobox on click
    $('.toggleInfobox').unbind('click').click(function () {
        $(this).prev().toggleClass('show-collapsed');
        $(this).toggleText('Collapse infobox', 'Expand infobox');
    })

    // Jump to headline in right tab with offset
    $('a[href^="#"]').unbind('click').click(function(event) {
        var hashValue = $(this).attr('href')

        // Prevent default behaviour and proceed below instead
        event.preventDefault();

        // collapse TOC on mobile
        $('.ms-toc').removeClass('ms-toc-active');

        handleAnchorLinks(hashValue);
    });

    //Trigger confetti
    $('.ms-inline-thanks').click(function(){
        $('#confetti').toggleClass('rain');
    }).mouseenter(function(){
        $('#confetti').toggleClass('rain');
    }).mouseleave(function(){
        $('#confetti').removeClass('rain');
    });

    //Show TOC on mobile
    $('.ms-tabs a.ms-trigger-toc').unbind('click').click(function(event) {
        $('.ms-toc').toggleClass('ms-toc-active');
    });
    $('.ms-article-top a.ms-button-toc').unbind('click').click(function(event) {
        $('.ms-toc').toggleClass('ms-toc-active');
    });


    $('article').click(function(event) {
        $('.ms-toc').removeClass('ms-toc-active');
    });

    // Toggle navigation bar
    $("#navToggle").unbind('click').click(function () {
        $("#navContent").slideToggle();
        $("#main-logo").fadeToggle();
    });

}


//
// Document ready calls
//-----------------------------------------------------------------

$(function() {

    //  delay for anchors to prevent wrong scrolling position
    if (location.hash) {
        var hashValue = location.hash
        handleAnchorLinks(hashValue);
    }
    else{
            console.log('Calling makeToC from Document ready')
        makeToC();
    }

    // Enable popover (inline references)
    $('[data-toggle="popover"]').popover();

    // Caluclate hights after DOM finished loading
    setTimeout(function() {
          // Collpase/Show Marginals
        collapseOversizedMarginals();
        collapseOversizedInfobox();

        // Normalise slide height
        normaliseSlidesHeight();
    }, 1000);


    $('body').scrollspy({ target: '.ms-toc', offset: 100 });

    // listner to toggle class
    enableListener();

});


