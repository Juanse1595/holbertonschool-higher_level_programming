$(() => {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: (data) => {
      $.each(data.results, (idx, value) => {
        $('#list_movies').append(`<li>${value.title}</li>`);
      });
    }
  });
});
