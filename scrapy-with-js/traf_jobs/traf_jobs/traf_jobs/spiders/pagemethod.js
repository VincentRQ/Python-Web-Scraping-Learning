const interval_id = setInterval( function(){
    const button = document.querySelector('#results > div.py-3.ng-star-inserted > button');
    if (button) {
        button.scrollIntoView();
        button.click();
    }
}, 1000)


