% include('header.tpl')
<a href="/projects">&laquo; Projects</a>
<table>
  <caption>Repositories list</caption>
  <thead>
    <tr>
      <th>Type</th>
      <th>URI</th>
    </tr>
  </thead>
  <tbody>
  % for repository in repositories:
    <tr>
      <td>{{repository['repo_type']}}</td>
      <td><a href="{{repository['repo_url']}}" target="_blank">{{repository['repo_url']}}</a></td>
  % end
  </tbody>
</table>
<p><a href="add_repo">Add data source &raquo;</a></p>
<p><a href="json">See json file</a></p>
% include('footer.tpl')
