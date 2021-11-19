<script>
  import Quote from "quoters";
  import { onMount } from "svelte";
  import Editor from "./Editor.svelte";
  let category = "QUOTE";
  export let quote = new Quote(category).get();
  function handleCategory(event) {
    category = event.target.dataset.category;
    quote = new Quote(category).get();
  }
</script>

<main>
  <div class="row  m-0 mt-3">
    <div
      class="
          col-lg-8 col-md-6
          rounded
          container
          border
          border-dark
        "
    >
      <h1 class="display-5 fw-bold">
        <u> <span class="display-4 fw-bold">q</span><span>uoters</span></u>
      </h1>
      <p class="lead text-body">
        A library that gives you beautiful quotes for multiple categories.
      </p>
    </div>
    <div
      class="
    col-lg-12 col-md-12
    rounded p-3 text-center"
    >
      <div class="h3">CATEGORIES</div>
      <p>
        <button
          class="btn btn-secondary category"
          data-category="QUOTE"
          on:click={handleCategory}
        >
          Life Quotes
        </button>
        <button
          class="btn btn-primary category"
          data-category="SERIES"
          on:click={handleCategory}
        >
          TV Series
        </button>
        <button
          class="btn btn-primary category"
          data-category="ANIME"
          on:click={handleCategory}
        >
          Anime
        </button>
        <button
          class="btn btn-primary category"
          data-category="PROGRAMMING"
          on:click={handleCategory}
        >
          Programming
        </button>
      </p>
    </div>
  </div>
  <Editor category={category}  />
  <div class="row py-3 m-0">
    <div
      class="
          col-lg-8 col-md-8
          mx-auto
          border
          rounded
          p-4
          fst-italic
          fs-4
          border-dark
        "
      id="quote"
    >
      {quote}
    </div>
  </div>
</main>
