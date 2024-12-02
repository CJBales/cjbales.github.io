$(document).ready(function() {
    // API root URL
    const apiUrl = "https://musicbrainz.org/ws/2/";

    // Function to fetch and display music facts based on a search query
    function searchMusic(query) {
        // Make sure the query is not empty
        if (!query) {
            alert("Please enter a search term.");
            return;
        }

        // Search for artists, albums, or songs using the MusicBrainz API
        $.ajax({
            url: `${apiUrl}artist`,
            method: "GET",
            data: {
                query: query,
                fmt: "json",
                limit: 5 // Limit to 5 results for simplicity
            },
            success: function(data) {
                // Clear existing results
                $('#content').empty();
                $('#top-artists').empty();
                
                // Display search results for artists
                if (data.artists && data.artists.length > 0) {
                    data.artists.forEach(artist => {
                        const artistInfo = `
                            <div class="result-item">
                                <strong>Artist: </strong><span>${artist.name}</span><br>
                                <strong>Type: </strong><span>${artist.type}</span><br>
                                <button class="view-albums" data-artist-id="${artist.id}">View Albums</button>
                                <button class="view-recordings" data-artist-id="${artist.id}">View Songs</button>
                            </div>`;
                        $('#content').append(artistInfo);
                    });
                } else {
                    $('#content').append("<p>No artists found for your search query.</p>");
                }
            },
            error: function(err) {
                console.log("Error searching for artists", err);
            }
        });

        // Now search for albums and songs with the same query
        $.ajax({
            url: `${apiUrl}release`,
            method: "GET",
            data: {
                query: query,
                fmt: "json",
                limit: 5
            },
            success: function(data) {
                // Display search results for albums
                if (data.releases && data.releases.length > 0) {
                    $('#content').append("<h3>Albums</h3>");
                    data.releases.forEach(release => {
                        const albumInfo = `
                            <div class="result-item">
                                <strong>Album: </strong><span>${release.title}</span><br>
                                <strong>Artist: </strong><span>${release.artist ? release.artist.name : "Unknown"}</span><br>
                                <strong>Release Date: </strong><span>${release.date}</span><br>
                            </div>`;
                        $('#content').append(albumInfo);
                    });
                } else {
                    $('#content').append("<p>No albums found for your search query.</p>");
                }
            },
            error: function(err) {
                console.log("Error searching for albums", err);
            }
        });

        // Finally, search for recordings (songs) that match the query
        $.ajax({
            url: `${apiUrl}recording`,
            method: "GET",
            data: {
                query: query,
                fmt: "json",
                limit: 5
            },
            success: function(data) {
                // Display search results for songs
                if (data.recordings && data.recordings.length > 0) {
                    $('#content').append("<h3>Songs</h3>");
                    data.recordings.forEach(recording => {
                        const songInfo = `
                            <div class="result-item">
                                <strong>Song: </strong><span>${recording.title}</span><br>
                                <strong>Artist: </strong><span>${recording.artist ? recording.artist.name : "Unknown"}</span><br>
                                <strong>Release Date: </strong><span>${recording.date}</span><br>
                            </div>`;
                        $('#content').append(songInfo);
                    });
                } else {
                    $('#content').append("<p>No songs found for your search query.</p>");
                }
            },
            error: function(err) {
                console.log("Error searching for songs", err);
            }
        });
    }

    // Handle search form submission
    $('#search-form').submit(function(event) {
        event.preventDefault();
        const query = $('#search-input').val().trim();
        searchMusic(query);
    });

    // Event listener for fetching albums or songs when the user clicks the buttons
    $(document).on('click', '.view-albums', function() {
        const artistId = $(this).data('artist-id');
        $.ajax({
            url: `${apiUrl}release`,
            method: "GET",
            data: {
                artist: artistId,
                fmt: "json",
                limit: 5
            },
            success: function(data) {
                $('#content').empty();
                if (data.releases && data.releases.length > 0) {
                    data.releases.forEach(release => {
                        const albumInfo = `
                            <div class="result-item">
                                <strong>Album: </strong><span>${release.title}</span><br>
                                <strong>Release Date: </strong><span>${release.date}</span><br>
                            </div>`;
                        $('#content').append(albumInfo);
                    });
                } else {
                    $('#content').append("<p>No albums found for this artist.</p>");
                }
            },
            error: function(err) {
                console.log("Error fetching albums", err);
            }
        });
    });

    $(document).on('click', '.view-recordings', function() {
        const artistId = $(this).data('artist-id');
        $.ajax({
            url: `${apiUrl}recording`,
            method: "GET",
            data: {
                artist: artistId,
                fmt: "json",
                limit: 5
            },
            success: function(data) {
                $('#content').empty();
                if (data.recordings && data.recordings.length > 0) {
                    data.recordings.forEach(recording => {
                        const songInfo = `
                            <div class="result-item">
                                <strong>Song: </strong><span>${recording.title}</span><br>
                                <strong>Release Date: </strong><span>${recording.date}</span><br>
                            </div>`;
                        $('#content').append(songInfo);
                    });
                } else {
                    $('#content').append("<p>No songs found for this artist.</p>");
                }
            },
            error: function(err) {
                console.log("Error fetching songs", err);
            }
        });
    });

});