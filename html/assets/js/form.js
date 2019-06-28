function submitForm() {
    let form = document.getElementById("form");
    let formData = new FormData(form);

    let urlParams = new URLSearchParams(window.location.search);
    let serverId = urlParams.get("server_id");

    formData.append("server_id", serverId)

    var request = new XMLHttpRequest();
    request.open("POST", "http://localhost:4343/submit");
    request.send(formData);
}