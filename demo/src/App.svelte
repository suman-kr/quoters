<script>
  import Quote from "quoters";
  import Editor from "./Editor.svelte";
  import Links from "./Links.svelte";
  import { fade, fly } from "svelte/transition";

  let category = "QUOTE";
  let visible = true;
  let quote = new Quote(category).get();
  function handleCategory(event) {
    category = event.target.dataset.category;
    quote = new Quote(category).get();
  }
</script>

<main>
  <div class="row  m-0 mt-3">
    <div class=" col-lg-8 col-md-6 rounded container border border-dark">
      <h1 class="display-5 fw-bold">
        <u> <span class="display-4 fw-bold">q</span><span>uoters</span></u>
      </h1>
      <p class="lead text-body">
        A library that gives you beautiful quotes for multiple categories.
      </p>
      <Links />
    </div>
    <div class=" col-lg-12 col-md-12  p-3 text-center">
      <div class="h3">CATEGORIES</div>
      <p>
        <button
          class={`btn category ${
            category === "QUOTE" ? "btn btn-secondary" : ""
          }`}
          data-category="QUOTE"
          on:click={handleCategory}
        >
          Life Quotes
        </button>
        <button
          class={`btn category ${
            category === "SERIES" ? "btn btn-secondary" : ""
          }`}
          data-category="SERIES"
          on:click={handleCategory}
        >
          TV Series
        </button>
        <button
          class={`btn category ${
            category === "ANIME" ? "btn btn-secondary" : ""
          }`}
          data-category="ANIME"
          on:click={handleCategory}
        >
          Anime
        </button>
        <button
          class={`btn category ${
            category === "PROGRAMMING" ? "btn btn btn-secondary" : ""
          }`}
          data-category="PROGRAMMING"
          on:click={handleCategory}
        >
          Programming
        </button>
      </p>
    </div>
  </div>
  <Editor category={category.toLowerCase()} />
  <div class="row py-3 m-0">
    {#if visible}
      <div
        class="col-lg-8 col-md-8 mx-auto border rounded p-4 fst-italic fs-4 border-dark"
        id="quote"
        in:fly={{ y: 100, duration: 2000 }}
        out:fade
      >
        {quote}
      </div>
    {/if}
  </div>
</main>
