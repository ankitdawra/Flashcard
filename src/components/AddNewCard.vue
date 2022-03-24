<template>
    <div class="container mt-5 mb-5">
        
        <div class="row justify-content-center">
            <h2 class="text-center"> Add New Card</h2>
            <h5 class="text-center"> to </h5>
            <h2 class="text-center"> <b> {{ deck.name }}</b></h2>
            <div class="card col-md-4"> 
                <form @submit.prevent="addNewCard">
                    <div class="form-group">
                      <label for="front">Question: </label>
                      <input type="text" class="form-control"  placeholder="Front" name="front">
                    </div>
                    <div class="form-group">
                      <label for="back">Answer: </label>
                      <input type="text" class="form-control"  placeholder="Back" name="back">
                    </div>
                    <br>
                    <div> 
                        <a href='/dashboard' type="button" class="btn btn-primary "> Go back to Decks </a>
                        <button type="submit" class="btn btn-primary active">Submit</button>
                    </div>
                        
                  </form>
            </div>   
        </div>
  
 
    </div>
</template>

<script> 

export default {
  name: 'AddNewCard',
  data() {
    return{ 
      deck : null,
        }
  },

methods: {
    async addNewCard() {
      const { front, back, deck_id } = this;
      const res = await fetch(
        "http://127.0.0.1:5000/card",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0ODExODAwNCwianRpIjoiZDJlNzlmYjMtNjQwNS00MTNhLTk2MDEtOWYxMmUxNzFjM2M0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjQ4MTE4MDA0LCJleHAiOjE2NDgxMTg5MDR9.5aBs7FrtaLmy0yKjSAvMc3Y2OFiyebewwXJGhU9VK-E`
          },
          body: JSON.stringify({ front, back, deck_id })
        }
      );
      const data = await res.json();
      console.log(data);
    }
  }};
</script>