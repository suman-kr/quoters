var ghpages = require("gh-pages");

ghpages.publish(
  "public",
  {
    branch: "gh-pages",
    repo: "https://github.com/suman-kr/quoters.git",
    user: {
      name: "Suman Kumar",
      email: "skcool.123bgp@gmail.com",
    },
  },
  () => {
    console.log("Deploy Complete!");
  }
);
