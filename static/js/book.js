// get all club approval buttons
const buttons = document.querySelectorAll('.book-appt-btn');

// add event listener for all buttons
for (const button of buttons){
    button.addEventListener('click', evt => {
        console.log('clicked');
        const data = {
            // get club_user_id from button id
            appt_time: evt.target.id
        }
        // send post request
        fetch('/book-appt', {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
                },
            })
            .then(response => response.text())
            // replace button text
            .then(result => {
                evt.target.innerHTML = result;
            });
    });
}