/*jslint browser: true*/
/*global $, jQuery, alert, console*/

/**
 * Horst.js - Refactored for improved efficiency and reliability
 * 
 * This refactor eliminates arbitrary timeout-based execution ordering
 * in favor of modern, event-driven approaches using:
 * - MutationObserver for DOM changes
 * - Intersection Observer for element visibility
 * - Promises for async operations
 * - Proper event listeners for load states
 */

// ToggleText function
$.fn.extend({
  toggleText: function (a, b) {
    return this.text(this.text() == b ? a : b);
  },
});

/**
 * Modern DOM utilities to replace timeout-based approaches
 */
const HorstUtils = {
  /**
   * Waits for an element to be available in the DOM
   * @param {string} selector - CSS selector for the element
   * @param {number} timeout - Maximum time to wait (default: 5000ms)
   * @returns {Promise<Element>} Promise that resolves when element is found
   */
  waitForElement: function(selector, timeout = 5000) {
    return new Promise((resolve, reject) => {
      const element = document.querySelector(selector);
      if (element) {
        resolve(element);
        return;
      }

      const observer = new MutationObserver((mutations, obs) => {
        const element = document.querySelector(selector);
        if (element) {
          obs.disconnect();
          resolve(element);
        }
      });

      observer.observe(document.body, {
        childList: true,
        subtree: true
      });

      // Timeout fallback
      setTimeout(() => {
        observer.disconnect();
        reject(new Error(`Element ${selector} not found within ${timeout}ms`));
      }, timeout);
    });
  },

  /**
   * Waits for elements to be fully rendered (dimensions available)
   * @param {string|jQuery} elements - CSS selector or jQuery object
   * @returns {Promise<void>} Promise that resolves when elements are rendered
   */
  waitForElementsRendered: function(elements) {
    return new Promise((resolve) => {
      const $elements = typeof elements === 'string' ? $(elements) : elements;
      
      if ($elements.length === 0) {
        resolve();
        return;
      }

      // Check if elements are already rendered
      let allRendered = true;
      $elements.each(function() {
        if ($(this).height() === 0 && $(this).width() === 0) {
          allRendered = false;
          return false; // break
        }
      });

      if (allRendered) {
        resolve();
        return;
      }

      // Use Intersection Observer to detect when elements are rendered
      const observer = new IntersectionObserver((entries) => {
        let renderedCount = 0;
        entries.forEach(entry => {
          if (entry.isIntersecting || entry.boundingClientRect.height > 0) {
            renderedCount++;
          }
        });

        if (renderedCount === entries.length) {
          observer.disconnect();
          resolve();
        }
      });

      $elements.each(function() {
        observer.observe(this);
      });

      // Fallback timeout
      setTimeout(() => {
        observer.disconnect();
        resolve();
      }, 2000);
    });
  },

  /**
   * Waits for images within elements to load
   * @param {string|jQuery} container - Container to check for images
   * @returns {Promise<void>} Promise that resolves when all images are loaded
   */
  waitForImages: function(container) {
    return new Promise((resolve) => {
      const $container = typeof container === 'string' ? $(container) : container;
      const $images = $container.find('img');

      if ($images.length === 0) {
        resolve();
        return;
      }

      let loadedCount = 0;
      const totalImages = $images.length;

      $images.each(function() {
        const img = this;
        if (img.complete && img.naturalHeight !== 0) {
          loadedCount++;
        } else {
          $(img).on('load error', function() {
            loadedCount++;
            if (loadedCount === totalImages) {
              resolve();
            }
          });
        }
      });

      if (loadedCount === totalImages) {
        resolve();
      }
    });
  },

  /**
   * Debounced function execution
   * @param {Function} func - Function to debounce
   * @param {number} wait - Debounce delay in milliseconds
   * @returns {Function} Debounced function
   */
  debounce: function(func, wait) {
    let timeout;
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout);
        func.apply(this, args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  }
};

/**
 * Normalise slide height to prevent jumping
 * Refactored to wait for proper element rendering before calculating heights
 */
async function normalizeSlideHeights() {
  try {
    const $carousels = $(".carousel");
    if ($carousels.length === 0) {
      console.log('No carousels found for height normalization');
      return;
    }

    // Wait for carousels to be properly rendered
    await HorstUtils.waitForElementsRendered($carousels);
    
    // Wait for any images in carousels to load
    await Promise.all($carousels.map(function(index, carousel) {
      return HorstUtils.waitForImages($(carousel));
    }).get());

    $carousels.each(function () {
      const $carousel = $(this);
      const $items = $(".carousel-item", this);
      
      if ($items.length === 0) {
        console.log('No carousel items found in carousel');
        return;
      }

      // Reset the height to get natural heights
      $items.css("min-height", "");
      
      // Calculate maximum height after a short delay to ensure rendering
      setTimeout(() => {
        const maxHeight = Math.max.apply(
          null,
          $items.map(function () {
            return $(this).outerHeight(true);
          }).get()
        );
        
        if (maxHeight > 0) {
          $items.css("min-height", maxHeight + "px");
          console.log(`Normalized carousel heights to ${maxHeight}px`);
        }
      }, 10);
    });
  } catch (error) {
    console.error('Error normalizing slide heights:', error);
    // Fallback to original approach if modern method fails
    $(".carousel").each(function () {
      var items = $(".carousel-item", this);
      items.css("min-height", 0);
      var maxHeight = Math.max.apply(
        null,
        items.map(function () {
          return $(this).outerHeight(true);
        }).get()
      );
      items.css("min-height", maxHeight + "px");
    });
  }
}

/**
 * Table of contents - Refactored for reliable async operation
 */
var selector;

// Control variable for TOC building behavior
// Set to true to build TOC on all tabs, false to build only on index tab
var buildTocOnAllTabs = false;

// Control variable for TOC depth (number of heading levels to include)
var TocDepth = 2;

/**
 * Modern, async Table of Contents builder
 * Waits for proper DOM state before building TOC
 */
async function makeToC() {
  try {
    console.log("Creating TOC with modern async approach...");
    
    // Wait for the target elements to be available
    await HorstUtils.waitForElement('.ms-toc');
    await HorstUtils.waitForElement('.tab-pane.active article');
    
    // Setup scroll spy attributes
    $("article").attr("data-spy", "scroll");
    $("body").attr("data-target", ".ms-toc");
    $("article").attr("data-offset", "-300");

    // Clear and setup TOC container
    const $tocContainer = $(".ms-toc");
    $tocContainer.empty();
    $tocContainer
      .append(
        '<ul class="ms-toc-entries nav nav-pills sticky-top flex-column side-nav" aria-hidden="false"></ul>'
      )
      .append(
        '<ul class="ms-toc-abstract-entries nav nav-pills sticky-top flex-column side-nav" aria-hidden="true"></ul>'
      );

    // Wait for TOC container elements to be rendered
    await HorstUtils.waitForElementsRendered($tocContainer);

    // Get headers from active tab
    selector = $(".tab-pane.active article :header");
    
    if (selector.length === 0) {
      console.log("No headers found for TOC building");
      return;
    }

    console.log(`Building TOC with ${selector.length} headers`);

    // Build TOC sections
    await buildTocSections();

    // Enable event listeners
    enableListener();
    
    console.log("TOC refreshed successfully");

    // Enable scrollspy on new TOC/page content with slight delay for DOM stability
    setTimeout(() => {
      $("body").scrollspy('dispose').scrollspy({ target: ".ms-toc", offset: 100 });
    }, 50);
    
  } catch (error) {
    console.error('Error building TOC:', error);
    // Fallback to original synchronous approach if async fails
    fallbackMakeToC();
  }
}

/**
 * Build TOC sections asynchronously
 */
async function buildTocSections() {
  // Wait for any images in the content to load (affects header positions)
  await HorstUtils.waitForImages($('.tab-pane.active article'));
  
  // Build both TOC variants
  addReduced();
  addDetailed();
}

/**
 * Fallback synchronous TOC builder for compatibility
 */
function fallbackMakeToC() {
  console.log("Using fallback synchronous TOC building");
  $("article").attr("data-spy", "scroll");
  $("body").attr("data-target", ".ms-toc");
  $("article").attr("data-offset", "-300");

  $(".ms-toc").empty();
  $(".ms-toc")
    .append(
      '<ul class="ms-toc-entries nav nav-pills sticky-top flex-column side-nav" aria-hidden="false"></ul>'
    )
    .append(
      '<ul class="ms-toc-abstract-entries nav nav-pills sticky-top flex-column side-nav" aria-hidden="true"></ul>'
    );

  selector = $(".tab-pane.active article :header");
  addReduced();
  addDetailed();
  enableListener();
  $("body").scrollspy({ target: ".ms-toc", offset: 100 });
}

// Build abstract lines
function addReduced() {
  // foreach header append a line
  for (var i = 0; i < selector.length; i++) {
    if ($(selector[i]).attr("id")) {
      // Add elements to nav
      for (var j = 2; j < 2 + TocDepth; j++) {
        if (selector[i].nodeName == "H" + j) {
          $("ul.ms-toc-abstract-entries").append(
            '<li class="nav-item side-nav ms-toc-abstract-entry ms-toc-abstract-entry ms-toc-abstract-entry-' +
              j +
              '"><a class="nav-link side-nav ms-toc-entry-link" href="#' +
              $(selector[i]).attr("id") +
              '"></a></li>'
          );
        }
      }
    }
  }
}

// Build full toc
function addDetailed() {
  // foreach header append a line
  for (var i = 0; i < selector.length; i++) {
    if ($(selector[i]).attr("id")) {
      // Add elements to nav
      for (var j = 2; j < 2 + TocDepth; j++) {
        if (selector[i].nodeName == "H" + j) {
          $("ul.ms-toc-entries").append(
            '<li class="nav-item side-nav ms-toc-entry ms-toc-entry-level' +
              j +
              '"><a class="nav-link side-nav ms-toc-entry-link" href="#' +
              $(selector[i]).attr("id") +
              '">' +
              selector[i].textContent +
              "</a></li>"
          );
        }
      }
    }
  }
}

/**
 * Collapse oversized marginal notes - Refactored for async operation
 */
async function collapseOversizedMarginals() {
  try {
    console.log("Collapsing oversized marginals with async approach...");
    
    // Wait for elements to be properly rendered before calculating heights
    const $textElements = $(".tab-pane.active .ms-text");
    if ($textElements.length === 0) {
      console.log("No text elements found for marginal collapse");
      return;
    }

    await HorstUtils.waitForElementsRendered($textElements);
    
    // Process each text element
    for (let i = 0; i < $textElements.length; i++) {
      const $element = $($textElements[i]);
      await processMarginalElement($element);
    }
    
    console.log("Marginal collapse completed successfully");
    
  } catch (error) {
    console.error('Error collapsing marginals:', error);
    // Fallback to original synchronous approach
    fallbackCollapseOversizedMarginals();
  }
}

/**
 * Process a single marginal element
 * @param {jQuery} $element - The text element to process
 */
async function processMarginalElement($element) {
  const numAsides = $element
    .children(".ms-col-marginal")
    .children("aside").length;

  /* Deal with marginals if exist */
  if (numAsides > 0) {
    // Wait for aside elements to be properly rendered
    const $asides = $element.children(".ms-col-marginal").children("aside");
    await HorstUtils.waitForElementsRendered($asides);
    
    let isOverflowing = false;
    let canOverflow = false;

    /* Content heights */
    let heightAsides = 0;
    $asides.each(function () {
      heightAsides += $(this).height();
    });

    const heightContent = $element
      .children(".ms-col-content")
      .children("p")
      .height();

    /* Check whitespace under content */
    if (heightAsides - heightContent > 20) {
      isOverflowing = true;
    }

    /* Check if there is no asides or plugins after overflowing, single aside */
    if ($element.next().hasClass("ms-text")) {
      if ($element.next().children(".ms-col-marginal").children().length === 0) {
        if (numAsides < 2) {
          canOverflow = true;
        }
      }
    }

    if (isOverflowing) {
      // if overflow possible, just set height of row
      if (canOverflow) {
        $element
          .children(".ms-col-marginal")
          .addClass("marginals-overflowing");
        $element.children(".ms-col-marginal").css("max-height", heightContent);
        $element
          .children(".ms-col-marginal")
          .children("aside")
          .addClass("show");
      }
      // otherwise start collapsing
      else {
        // set height of marginal to be no more than content
        $element.children(".ms-col-marginal").addClass("marginals-collapsed");
        $element.children(".ms-col-marginal").css("max-height", heightContent);

        /* Calculate aside height */
        const currentNumAsides = $element
          .children(".ms-col-marginal")
          .children("aside").length;

        let medHeightAsides = heightContent / currentNumAsides;
        medHeightAsides = medHeightAsides - 10;

        $element
          .children(".ms-col-marginal")
          .children("aside")
          .each(function () {
            const $aside = $(this);
            if ($aside.children("p").height() < medHeightAsides) {
              $aside.css("flex-shrink", 0);
              $aside.css("flex-grow", 0);
              $aside.css("flex-basis", $aside.children("p").height());
              $aside.addClass("show");
            } else {
              $aside.css("flex-shrink", 1);
              $aside.css("flex-basis", medHeightAsides);
              $aside.addClass("collapsed");
            }
          });
      }
    } else {
      $element.children(".ms-col-marginal").children("aside").addClass("show");
    }
  }
}

/**
 * Fallback synchronous marginal collapse
 */
function fallbackCollapseOversizedMarginals() {
  console.log("Using fallback synchronous marginal collapse");
  
  $(".tab-pane.active .ms-text").each(function () {
    var numAsides = $(this)
      .children(".ms-col-marginal")
      .children("aside").length;

    /* Deal with marginals if exist */
    if (numAsides > 0) {
      var isOverflowing = false;
      var canOverflow = false;

      /* Content heights */
      var heightAsides = 0;
      $(this)
        .children(".ms-col-marginal")
        .children("aside")
        .each(function () {
          heightAsides = heightAsides + $(this).height();
        });

      var heightContent = $(this)
        .children(".ms-col-content")
        .children("p")
        .height();

      /* Check whitespace under content */
      if (heightAsides - heightContent > 20) {
        isOverflowing = true;
      }

      /* Check if there is no asides or plugins after overflowing, single aside */
      if ($(this).next().hasClass("ms-text")) {
        if (
          $(this).next().children(".ms-col-marginal").children().length == 0
        ) {
          if (numAsides < 2) {
            canOverflow = true;
          }
        }
      }

      if (isOverflowing) {
        // if overflow possible, just set height of row
        if (canOverflow) {
          $(this)
            .children(".ms-col-marginal")
            .addClass("marginals-overflowing");
          $(this).children(".ms-col-marginal").css("max-height", heightContent);
          $(this)
            .children(".ms-col-marginal")
            .children("aside")
            .addClass("show");
        }
        // otherwise start collapsing
        else {
          // set height of marginal to be no more than content
          $(this).children(".ms-col-marginal").addClass("marginals-collapsed");
          $(this).children(".ms-col-marginal").css("max-height", heightContent);

          /* Calculate aside height */
          numAsides = $(this)
            .children(".ms-col-marginal")
            .children(" aside").length;

          var medHeightAsides = heightContent / numAsides;
          medHeightAsides = medHeightAsides - 10;

          $(this)
            .children(".ms-col-marginal")
            .children(" aside")
            .each(function () {
              if ($(this).children("p").height() < medHeightAsides) {
                $(this).css("flex-shrink", 0);
                $(this).css("flex-grow", 0);
                $(this).css("flex-basis", $(this).children("p").height());
                $(this).addClass("show");
              } else {
                $(this).css("flex-shrink", 1);
                $(this).css("flex-basis", medHeightAsides);
                $(this).addClass("collapsed");
              }
            });
        }
      } else {
        $(this).children(".ms-col-marginal").children("aside").addClass("show");
      }
    }
  });
}

/**
 * Collapse oversized infobox - Refactored for async operation
 */
async function collapseOversizedInfobox() {
  try {
    console.log("Collapsing oversized infoboxes...");
    
    const $infoboxes = $(".ms-plugin-infobox");
    if ($infoboxes.length === 0) {
      console.log("No infoboxes found");
      return;
    }
    
    await HorstUtils.waitForElementsRendered($infoboxes);
    
    $infoboxes.each(function () {
      let isOverflowing = false;
      let canOverflow = false;
      const maxHeight = 200;

      /* Check height */
      const heightContent = $(this).height();
      if (heightContent > maxHeight) {
        isOverflowing = true;
      }

      /* Check if collapse is set to true > class collapse exists */
      if ($(this).hasClass("collapse")) {
        canOverflow = true;
      }

      if (isOverflowing) {
        // if collapse set to true, adjust class and show button
        if (canOverflow) {
          $(this).addClass("infobox-overflowing");
          $(this).after(
            '<button class="btn btn-primary toggleInfobox" type="button">Expand infobox</button>'
          );
        }
      }
    });
    
    // Re-enable listeners after adding new buttons
    enableListener();
    
    console.log("Infobox collapse completed");
    
  } catch (error) {
    console.error('Error collapsing infoboxes:', error);
    // Fallback approach
    $(".ms-plugin-infobox").each(function () {
      var isOverflowing = false;
      var canOverflow = false;
      var maxHeight = 200;

      var heightContent = $(this).height();
      if (heightContent > maxHeight) {
        isOverflowing = true;
      }

      if ($(this).hasClass("collapse")) {
        canOverflow = true;
      }

      if (isOverflowing) {
        if (canOverflow) {
          $(this).addClass("infobox-overflowing");
          $(this).after(
            '<button class="btn btn-primary toggleInfobox" type="button">Expand infobox</button>'
          );
        }
        enableListener();
      }
    });
  }
}

/**
 * Handle anchor links - Refactored for async operation
 */

/**
 * Changes to a tab using modern async approach
 * @param {jQuery} prevTab - Previously active tab
 * @param {jQuery} targetTab - Tab to switch to
 * @param {boolean} noscroll - Whether to prevent scrolling
 */
async function changeToTab(prevTab, targetTab, noscroll = false) {
  const offset = 80;

  console.log("Changing tabs with async approach");

  // Show tab manually to avoid collision with carousel
  // (bootstrap throws error, used try catch to continue script)
  try {
    prevTab.removeClass("active fade show");
    $(prevTab.attr("href")).removeClass("active");

    targetTab.addClass("active fade show");
    $(targetTab.attr("href")).addClass("active");
  } catch (err) {
    console.log("Changing tab errors: ", err);
  }

  try {
    // Update URL hash to track tab change for direct linking
    const targetTabId = targetTab.attr("href");
    if (targetTabId && targetTabId.startsWith("#")) {
      window.location.hash = targetTabId;
    }

    // Wait for tab transition to complete
    await new Promise(resolve => {
      // Check if tab content is visible and rendered
      const checkTabReady = () => {
        const $targetPane = $(targetTab.attr("href"));
        if ($targetPane.hasClass("active") && $targetPane.is(":visible")) {
          resolve();
        } else {
          setTimeout(checkTabReady, 10);
        }
      };
      checkTabReady();
    });

    // Reload TOC and collapse/show marginals after changing tabs
    const operations = [];
    
    if (buildTocOnAllTabs) {
      operations.push(makeToC());
    }
    
    operations.push(collapseOversizedMarginals());
    
    // Wait for all operations to complete
    await Promise.all(operations);

    // Handle scrolling after tab operations are complete - restore proper offset behavior
    if (!noscroll) {
      // Use requestAnimationFrame for smooth scrolling
      requestAnimationFrame(() => {
        try {
          window.scrollBy(0, -offset);
          // Scroll to the first content element in the active tab
          const firstElement = document.querySelector('.tab-pane.active .ms-text:first-child, .tab-pane.active article:first-child');
          if (firstElement) {
            firstElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
        } catch (scrollErr) {
          console.log('Scrolling error:', scrollErr);
        }
      });
    }

    console.log("Tab change completed successfully");
    
  } catch (error) {
    console.error('Error in tab change:', error);
    // Fallback to original timeout-based approach if async fails
    fallbackChangeToTab(prevTab, targetTab, noscroll);
  }
}

/**
 * Fallback synchronous tab change for compatibility
 */
function fallbackChangeToTab(prevTab, targetTab, noscroll = false) {
  const offset = 80;
  
  console.log("Using fallback synchronous tab change");
  
  // Update URL hash to track tab change
  const targetTabId = targetTab.attr("href");
  if (targetTabId && targetTabId.startsWith("#")) {
    window.location.hash = targetTabId;
  }
  
  if (buildTocOnAllTabs) {
    setTimeout(makeToC, 200);
  }
  setTimeout(() => collapseOversizedMarginals(), 300);

  if (!noscroll) {
    setTimeout(function () {
      scrollBy(0, -offset);
      // Scroll to the first content element in the active tab
      const firstElement = document.querySelector('.tab-pane.active .ms-text:first-child, .tab-pane.active article:first-child');
      if (firstElement) {
        firstElement.scrollIntoView(true);
      }
    }, 0);
  }
}

/**
 * Handle anchor links with modern async approach
 * @param {string} hashValue - The hash value from URL
 */
async function handleAnchorLinks(hashValue) {
  let activeTab = $("#masterTab a").filter(".active");

  try {
    if ($(hashValue).hasClass("tab-pane") && hashValue.includes("quote")) {
      console.log("Clicked a Quote tab");
      var tabID = "#" + $(hashValue).parents(".tab-pane").attr("id");
      await changeToTab(activeTab, $(tabID), true); // noscroll = true for quotes
      
    } else if ($(hashValue).hasClass("tab-pane")) {
      console.log("Clicked a tab");
      await changeToTab(activeTab, $("a[href='" + hashValue + "']"));
      
    } else {
      // Check if hash refers to a heading element
      var targetElement = $(hashValue);
      if (targetElement.length > 0 && targetElement.is(":header")) {
        console.log("Clicked a heading");

        var tabID = "#" + targetElement.parents(".tab-pane").attr("id");
        
        if (tabID && tabID !== "#") {
          // Switch to the correct tab first
          var targetTab = $("a[href='" + tabID + "']");
          if (targetTab.length > 0) {
            await changeToTab(activeTab, targetTab);
            
            // Scroll to the heading after tab switch is complete - restore 100px offset
            await scrollToElement(targetElement, 100);
          }
        } else {
          // Heading is in the current active tab, just build TOC if needed
          if (buildTocOnAllTabs) {
            await makeToC();
          }
          
          // Scroll to the heading - restore 100px offset like original
          await scrollToElement(targetElement, 100);
        }
      } else {
        // If hash is unknown, still build TOC if configured to do so
        console.log("hash unknown, building TOC if configured");
        if (buildTocOnAllTabs) {
          await makeToC();
        }
      }
    }

    // Set hash after all operations complete - ensure URL tracking works
    if (!window.location.hash || window.location.hash !== hashValue) {
      window.location.hash = hashValue;
    }
    
  } catch (error) {
    console.error('Error handling anchor links:', error);
    // Fallback to setting hash anyway
    if (!window.location.hash || window.location.hash !== hashValue) {
      window.location.hash = hashValue;
    }
  }
}

/**
 * Smooth scroll to element with proper timing - consistent 100px offset
 * @param {jQuery} $element - Element to scroll to
 * @param {number} offset - Offset from top in pixels (default: 100px to match original)
 */
async function scrollToElement($element, offset = 100) {
  return new Promise((resolve) => {
    // Wait for element to be visible and properly positioned
    const checkAndScroll = () => {
      if ($element.is(':visible') && $element.offset()) {
        const elementTop = $element.offset().top;
        $('html, body').animate({
          scrollTop: elementTop - offset
        }, {
          duration: 300,
          complete: resolve
        });
      } else {
        // Element not ready, wait a bit more
        setTimeout(checkAndScroll, 50);
      }
    };
    
    checkAndScroll();
  });
}

//
// Event listener
//---------------------------------------------------------------

function enableListener() {
  // Tab-button on mobile
  $(".tab-item").click(function (value) {
    $("#dropdownMenuButton").text($(this).text());
  });

  // Pause Carousel

  // $(".carousel").carousel('pause');
  // $('.carousel-item .ms-col-content').click(function(){
  //     if ($(this).parents('.carousel').hasClass('paused')) {
  //         $(this).parents('.carousel-item').addClass('play').delay(800).queue(function() {
  //             $(this).removeClass('play').dequeue();
  //         });
  //         $(this).parents('.carousel').toggleClass('paused');
  //         $(this).parents('.carousel').carousel('cycle');
  //         $(this).parents('.carousel').delay(500).queue(function() {
  //             $(this).carousel('next').dequeue();
  //         });
  //     }
  //     else{
  //         $(this).parents('.carousel-item').addClass('pause').delay(800).queue(function(){
  //             $(this).removeClass('pause').dequeue();
  //         });
  //         $(this).parents('.carousel').toggleClass('paused');
  //         $(this).parents('.carousel').carousel('pause');
  //     }
  // });

  // Show collapsed marginals on click
  $(".marginals-collapsed")
    .children("aside")
    .unbind("click")
    .click(function () {
      $(this).toggleClass("show-collapsed");
    });

  $(".marginals-collapsed")
    .children("aside")
    .mouseleave(function () {
      $(this).removeClass("show-collapsed");
    });

  // Toggle infobox on click
  $(".toggleInfobox")
    .unbind("click")
    .click(function () {
      $(this).prev().toggleClass("show-collapsed");
      $(this).toggleText("Collapse infobox", "Expand infobox");
    });

  // Jump to headline in right tab with offset
  $('a[href^="#"], a[href^="/#"]')
    .unbind("click")
    .click(function (event) {
      var hashValue = $(this).attr("href");
      hashValue = hashValue.replace(/^\//, ""); // Remove the initial "/"

      // Prevent default behaviour and proceed below instead
      event.preventDefault();

      // collapse TOC on mobile
      $(".ms-toc").removeClass("ms-toc-active");

      handleAnchorLinks(hashValue);
    });

  //Trigger confetti
  $(".ms-inline-thanks")
    .click(function () {
      $("#confetti").toggleClass("rain");
    })
    .mouseenter(function () {
      $("#confetti").toggleClass("rain");
    })
    .mouseleave(function () {
      $("#confetti").removeClass("rain");
    });

  //Show TOC on mobile
  $(".ms-tabs a.ms-trigger-toc")
    .unbind("click")
    .click(function (event) {
      $(".ms-toc").toggleClass("ms-toc-active");
    });
  $(".ms-article-top a.ms-button-toc")
    .unbind("click")
    .click(function (event) {
      $(".ms-toc").toggleClass("ms-toc-active");
    });

  $("article").click(function (event) {
    $(".ms-toc").removeClass("ms-toc-active");
  });

  // Toggle navigation bar
  $("#navToggle")
    .unbind("click")
    .click(function () {
      $("#navContent").slideToggle();
      $("#main-logo").fadeToggle();
    });
}

//
// Fix Bootstrap modal/carousel conflicts
//-------------------------------------------------------------

function fixModalCarouselConflicts() {
  // Store original modal positions
  var modalOriginalParents = {};
  
  // Handle modal show event
  $('body').on('show.bs.modal', '.modal', function (e) {
    var modal = $(this);
    var modalId = modal.attr('id');
    
    // Check if modal is inside a carousel
    var carousel = modal.closest('.carousel');
    if (carousel.length > 0) {
      // Store original parent and position
      modalOriginalParents[modalId] = {
        parent: modal.parent(),
        nextSibling: modal.next()[0] // Store DOM element for insertBefore
      };
      
      // Move modal to body to avoid carousel containment
      modal.appendTo('body');
      
      // Ensure modal has proper z-index
      modal.css('z-index', '1060');
    }
  });
  
  // Handle modal hidden event
  $('body').on('hidden.bs.modal', '.modal', function (e) {
    var modal = $(this);
    var modalId = modal.attr('id');
    
    // Check if we moved this modal
    if (modalOriginalParents[modalId]) {
      var originalInfo = modalOriginalParents[modalId];
      
      // Move modal back to original position
      if (originalInfo.nextSibling) {
        originalInfo.parent[0].insertBefore(modal[0], originalInfo.nextSibling);
      } else {
        originalInfo.parent.append(modal);
      }
      
      // Reset z-index
      modal.css('z-index', '');
      
      // Clean up stored info
      delete modalOriginalParents[modalId];
    }
  });
}

/**
 * Document ready calls - Refactored for modern async initialization
 */

/**
 * Modern async initialization function
 */
async function initializeHorst() {
  try {
    console.log("Starting modern Horst initialization...");

    // Always build TOC first to ensure proper structure
    console.log("Building initial TOC...");
    await makeToC();

    // Initialize layout first to ensure proper element sizing
    await initializeLayout();

    // Handle initial anchors after everything is set up - this fixes reload issues
    if (location.hash) {
      const hashValue = location.hash;
      console.log("Handling initial hash:", hashValue);
      // Wait longer for DOM to be fully settled before handling anchors on reload
      await new Promise(resolve => setTimeout(resolve, 200));
      await handleAnchorLinks(hashValue);
    }

    // Enable popover (inline references)
    $('[data-toggle="popover"]').popover();

    // Fix modal/carousel conflicts
    fixModalCarouselConflicts();

    // Enable scrollspy after everything is set up
    $("body").scrollspy({ target: ".ms-toc", offset: 100 });

    // Enable event listeners
    enableListener();
    
    console.log("Horst initialization completed successfully");
    
  } catch (error) {
    console.error('Error during Horst initialization:', error);
    // Fallback to original approach if modern initialization fails
    fallbackInitialization();
  }
}

/**
 * Initialize layout elements with proper async timing
 */
async function initializeLayout() {
  console.log("Initializing layout with async approach...");
  
  // Wait for DOM to be fully rendered
  await HorstUtils.waitForElementsRendered($('body'));
  
  // Initialize layout operations in parallel where safe
  const layoutOperations = [
    collapseOversizedMarginals(),
    collapseOversizedInfobox(),
    normalizeSlideHeights()
  ];
  
  // Wait for all layout operations to complete
  await Promise.all(layoutOperations);
  console.log("Layout initialization completed");
}

/**
 * Fallback initialization for compatibility
 */
function fallbackInitialization() {
  console.log("Using fallback initialization approach");
  
  // Handle initial anchors like original
  if (location.hash) {
    var hashValue = location.hash;
    handleAnchorLinks(hashValue);
  } else {
    console.log("Calling makeToC from fallback initialization");
    makeToC();
  }

  // Enable popover (inline references)
  $('[data-toggle="popover"]').popover();

  // Fix modal/carousel conflicts
  fixModalCarouselConflicts();
  
  // Original timeout-based approach as backup
  setTimeout(function () {
    collapseOversizedMarginals();
    collapseOversizedInfobox();
    normalizeSlideHeights();
  }, 600);

  $("body").scrollspy({ target: ".ms-toc", offset: 100 });
  enableListener();
}

// Modern document ready with async initialization
$(function () {
  // Use async initialization
  initializeHorst();
});

// Debounced resize handler for better performance
$(window).on(
  'resize orientationchange',
  HorstUtils.debounce(function() {
    console.log("Window resized, recalculating layouts...");
    normalizeSlideHeights();
    // Optionally recalculate other layout elements
    collapseOversizedMarginals();
  }, 250)
);