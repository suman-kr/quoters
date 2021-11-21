<script>
  let iconList = [
    {
      icon: "fab fa-github icon mx-2 cursor-pointer",
      link: "https://github.com/suman-kr/quoters",
      text: "",
    },
    {
      icon: "fas fa-code-branch icon-sm mx-2 cursor-pointer",
      link: "https://github.com/suman-kr/quoters/fork",
      text: "Fork on GitHub",
    },
    {
      icon: "fab fa-python icon mx-2 cursor-pointer",
      link: "https://pypi.org/project/quoters/",
      text: "",
    },
    {
      icon: "fab fa-npm icon mx-2 cursor-pointer",
      link: "https://www.npmjs.com/package/quoters",
      text: "",
    },
  ];
</script>

<div class="link-container">
  {#each iconList as { icon, link, text }}
    <div class="text-center">
      <a href={link}
        ><i class={icon} />
        {#if text}
          <div style="margin-top: -5px;">{text}</div>
        {/if}
      </a>
    </div>
  {/each}
</div>
