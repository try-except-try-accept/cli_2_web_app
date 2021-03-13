async function get_cli(url) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: 'GET', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'include', // include, *same-origin, omit
    headers: new Headers({
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    }),
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url

  });
  return response.json(); // parses JSON response into native JavaScript objects
}

function load_text(text)
{
    let output_textarea = document.getElementById("output")
    output_textarea.value = text;
}

function get_cli_output()
{
  fetch(`http://127.0.0.1:5000/get_cli`,  {
    method: "GET",
    credentials: "include",

    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json",
//        "SameSite": "strict",
//        "AccessControlAllowOrigin": "http://127.0.0.1:5000"
    })
  })
  .then(response => response.json())
  .then(response => load_text(response.message));

}

function send_cli_input()
{
    let input = document.getElementById("input")
    fetch(`http://127.0.0.1:5000/post_cli`,  {
    method: "POST",
    credentials: "include",
    body: JSON.stringify(input),
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', //

    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json",
//        "SameSite": "strict",
//        "AccessControlAllowOrigin": "http://127.0.0.1:5000"
    })
  })
  .then(response => response.json())
  .then(response => get_cli_output());

}

