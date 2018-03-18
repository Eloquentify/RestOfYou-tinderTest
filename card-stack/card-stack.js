const config = {
  /**
   * Invoked in the event of dragmove.
   * Returns a value between 0 and 1 indicating the completeness of the throw out condition.
   * Ration of the absolute distance from the original card position and element width.
   *
   * @param {number} xOffset Distance from the dragStart.
   * @param {number} yOffset Distance from the dragStart.
   * @param {HTMLElement} element Element.
   * @returns {number}
   */
  throwOutConfidence: (xOffset, yOffset, element) => {
    const xConfidence = Math.min(Math.abs(xOffset) / element.offsetWidth, 1);
    const yConfidence = Math.min(Math.abs(yOffset) / element.offsetHeight, 1);

    return Math.max(xConfidence, yConfidence);
  }
};
var start, end;
document.addEventListener('DOMContentLoaded', function () {
    var stack, card;
    stack = window.swing.Stack(config);

    [].forEach.call(document.querySelectorAll('.stack img'), function (targetElement) {
        card = stack.createCard(targetElement);

        targetElement.classList.add('in-deck');
    });

    stack.on('throwout', function (e) {

        // e.target Reference to the element that has been thrown out of the stack.
        // e.throwDirection Direction in which the element has been thrown (Direction.LEFT, Direction.RIGHT).
        console.log('out');
        console.log(e.target.src);
        console.log(e.throwDirection);
        e.target.classList.remove('in-deck');
    });
    stack.on('throwoutend', function(e){
      e.target.parentNode.removeChild(e.target);
    });

    stack.on('throwin', function (e) {
        console.log('in');
        console.log(e.target.src);
        console.log(e.throwDirection);

        e.target.classList.add('in-deck');
    });
    
    stack.on('dragstart', function (e) {
        start = new Date().getTime();
        //console.log('dragging start',start);
        // throwOutConfidenceElements.yes = e.target.querySelector('.yes').style;
        // throwOutConfidenceElements.no = e.target.querySelector('.no').style;
    });

    stack.on('dragmove', function (e) {
        //throwOutConfidenceElements[e.throwDirection == gajus.Swing.Card.DIRECTION_RIGHT ? 'yes' : 'no'].opacity = e.throwOutConfidence;

        //throwOutConfidenceBind.innerHTML = e.throwOutConfidence.toFixed(3);
        //directionBind.innerHTML = e.throwDirection.toString();
        //console.log('direction',e.throwDirection.toString());
    });

    stack.on('dragend', function (e) {
      end = new Date().getTime();
      //console.log('dragging time');
      console.log(end-start);
        // if (e.throwOutConfidence != 1) {
        //     throwOutConfidenceElements.yes.opacity = 0;
        //     throwOutConfidenceElements.no.opacity = 0;
        // }
    });
});
