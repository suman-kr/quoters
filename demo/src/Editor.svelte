<script>
  export let category;

  import "./style.scss";
  import pythonCode from "./data/python.json";
  import jsCode from "./data/javascript.json";
  import { onMount } from "svelte";
  let language = "python";
  let code = pythonCode.code;
  if (language === "python") {
    code = pythonCode.code;
  } else {
    code = jsCode.code;
  }

  $: codeSnippet = () => {
    return Object.keys(code.quote).map((key) => {
      return `${code.quote[key]}\n`;
    });
  };

</script>

<!-- <div class="row m-0 py-3"> -->
<div class="editor-container">
  <div class="editor rounded">
    <div class="editor-bar">Python 3</div>
    <div class="editor-content">
      <pre
        class="m-0">
        <code class="language-python">
        {#each codeSnippet() as snippet, index}
          {snippet}
      {/each}
    </code>
      </pre>
    </div>

    <!-- <code> {JSON.stringify(code.quote[1])} </code>
    <br />
    <code> {JSON.stringify(code.quote[2])} </code> -->
  </div>
</div>
<!-- </div> -->
