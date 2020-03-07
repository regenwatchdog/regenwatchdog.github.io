---
layout: page
---
{% for estate in site.estates %}
  <h2>{{ estate.name }}</h2>
    <p>{{ estate.content | markdownify }}</p>
    {% endfor %}
