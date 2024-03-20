// highlight the current date
document.addEventListener('DOMContentLoaded', function () {
    let currentDate = new Date();
    let currentYear = currentDate.getFullYear();
    let currentMonth = currentDate.getMonth() + 1; // Months are zero-indexed, so adding 1
    let currentDay = currentDate.getDate();
    
    let currentCell = document.getElementById(`day_${currentDay}`);

    // Add the 'current-date' class to the current cell if found
    if (currentCell) {
        currentCell.classList.add('current-date');
    }
});


// handling the prev and next buttons
document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('prevMonthBtn').addEventListener('click', function () {
        let currentYear = parseInt(document.querySelector('.calendar-container').dataset.year);
        let currentMonth = parseInt(document.querySelector('.calendar-container').dataset.month);

        if (currentMonth === 1) {
            currentYear -= 1;
            currentMonth = 12;
        } else {
            currentMonth -= 1;
        }
        
        updateCalendarData(currentYear, currentMonth);

        // Redirect or perform any action you want for navigating to the previous month
        console.log('Navigating to previous month:', currentYear, currentMonth);
    });

    document.getElementById('nextMonthBtn').addEventListener('click', function () {
        let currentYear = parseInt(document.querySelector('.calendar-container').dataset.year);
        let currentMonth = parseInt(document.querySelector('.calendar-container').dataset.month);
        
        if (currentMonth === 12) {
            currentYear += 1;
            currentMonth = 1;
        } else {
            currentMonth += 1;
        }
        
        updateCalendarData(currentYear, currentMonth);
        // Redirect or perform any action you want for navigating to the next month
        console.log('Navigating to next month:', currentYear, currentMonth);
    });

    function updateCalendarData(year, month) {
        // Send AJAX request to the server
        let xhr = new XMLHttpRequest();
        xhr.open('GET', `/update-calendar/${year}/${month}`, true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                // Handle the response if needed
                console.log('Calendar data updated successfully');
            }
        };
        xhr.send();
    }
    
});

