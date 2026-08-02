document.addEventListener("DOMContentLoaded", () => {

    document.body.style.opacity = "0";

    setTimeout(() => {
        document.body.style.transition = "opacity 1s";
        document.body.style.opacity = "1";
    }, 100);

    const buttons = document.querySelectorAll(".menu-btn");

    buttons.forEach(button => {

        button.addEventListener("click", () => {

            button.style.transform = "scale(0.96)";

            setTimeout(() => {
                button.style.transform = "scale(1)";
            }, 120);

        });

    });

});
