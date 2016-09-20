% include('header.tpl')
<h1>Projects</h1>
<ul>
% for project in projects:
  <li><a href="project/{{project['pid']}}/">{{project['pname']}}</li>
% end
</ul>
<a href="./add_project">Add project</a>
% include('footer.tpl')
