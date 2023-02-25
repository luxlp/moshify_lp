collapsibles = document.querySelectorAll(".collapsible")
for item in collapsibles:
    item.addEventListener("click", lambda: this.classList.toggle("collapsible--expanded"))