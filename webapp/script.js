document.addEventListener("DOMContentLoaded", () => {

    console.log("UNDERDOGG SYSTEM ONLINE");


    const buttons = document.querySelectorAll(".menu-btn");


    buttons.forEach(button => {

        button.addEventListener("click", () => {

            button.style.transform = "scale(0.95)";

            setTimeout(() => {

                button.style.transform = "scale(1)";

            },150);


            console.log(
                "ACCESS:",
                button.innerText
            );

        });

    });


});
