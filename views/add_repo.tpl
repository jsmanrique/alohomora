% include('header.tpl')
<form action="add_repo" method="post">
  <p><label for="datasource">Select data source type:</label>
    <select id="datasource" name="repo_type">
      <option value="git">git repo</option>
      <option value="github">GitHub organization</option>
      <option value="bugzilla">Bugzilla</option>
      <option value="mailman">Mailman mailing list</option>
    </select>
  </p>
   <p><label for="uri">Repository URI: <input id="uri" type="text" name="repo_url" placeholder="Data source URI"/></label>
  <p><input value="Add" type="submit" /></p>
</form>
% include('footer.tpl')
