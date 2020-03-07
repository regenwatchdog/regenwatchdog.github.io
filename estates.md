---
layout: page
---
{% for estate in site.estates %}
  <h2>{{ estate.name }} - {{ estate.borough }}</h2>
    <p>{{ estate.content | markdownify }}</p>
    {% endfor %}
