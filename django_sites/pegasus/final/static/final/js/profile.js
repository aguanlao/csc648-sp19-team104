function thetab(){
    const nav = document.getElementById("mynavmenu");
    let tabs = nav.getElementsByClassName("mytab");

    for (let i = 0; i < tabs.length; i++){
        tabs[i].addEventListener("click", function() {
        let current = document.getElementsByClassName(" active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
        });
    }
}