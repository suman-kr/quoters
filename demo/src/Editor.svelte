<script>
  export let category;
  import Highlight from "svelte-highlight";
  import github from "svelte-highlight/src/styles/github-dark";
  import pythonCode from "./data/python.json";
  import jsCode from "./data/javascript.json";
  import python from "svelte-highlight/src/languages/python";
  import javascript from "svelte-highlight/src/languages/javascript";
  let code = pythonCode.code;
  let language = python;
  let selectedLang = "python";
  $: codeSnippet = Object.keys(code[category]).map((key) => {
    return `${code[category][key]}\n`;
  });

  function handleCopy() {
    navigator.clipboard.writeText(codeSnippet.join(""));
  }

  function handleLanguageChange(lang) {
    if (lang === "python") {
      code = pythonCode.code;
      selectedLang = lang;
      language = python;
    } else {
      code = jsCode.code;
      selectedLang = lang;
      language = javascript;
    }
  }
</script>

<svelte:head>
  {@html github}
</svelte:head>
<div class="editor-container">
  <div class="editor rounded">
    <div class="editor-bar">
      <div class="language-toolbar">
        <div class="first-lang-option px-2 ">
          <span
            class={`cursor-pointer ${
              selectedLang === "python" ? "selected-option" : ""
            }`}
            on:click={() => handleLanguageChange("python")}>Python</span
          >
        </div>
        <div class="second-lang-option px-2 ">
          <span
            class={`cursor-pointer ${
              selectedLang === "javascript" ? "selected-option" : ""
            } `}
            on:click={() => handleLanguageChange("javascript")}>Node</span
          >
        </div>
        <div>
          <span on:click={handleCopy} title="Click to copy"
            ><i class="far fa-copy cursor-pointer" /></span
          >
        </div>
      </div>
      <div class="row m-0" />
    </div>
    <div class="editor-content">
      <Highlight code={codeSnippet.join("")} {language} />
    </div>
  </div>
</div>
