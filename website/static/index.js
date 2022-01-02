function deleteNote(noteId) {
  //to send a request in javascript use fetch
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    //reload window
    window.location.href = "/";
  });
}
