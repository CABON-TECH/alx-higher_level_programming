#!/usr/bin/node

const request = require('request');

const API_URL = process.argv[2];
const characterId = 18;

request(API_URL, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const filmsWithWedge = films.filter(film => {
      return film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`);
    });
    console.log(`Wedge Antilles appears in ${filmsWithWedge.length} films.`);
  }
});
