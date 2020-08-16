document.addEventListener("DOMContentLoaded", function () {
    console.log("hi");

})

var scrollToId = function (id) {
    console.log(id);
    document.getElementById(id).scrollIntoView({block: "start",  behavior: "smooth"});
}