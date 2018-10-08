<link  type="text/css" href="/static/tafla.css" rel="stylesheet">
<h1> Félagið </h1>
<p> Dagsetning uppfærslu {{!dagsetning}} </p>
<p> Fjöldi stöðva {{!fjoldi_st}}</p>

<table>
	<tr>
			<th>Félag </th><th>Stöð</th><th>Verð á bensíni</th>
	</tr>
	%for r in rows_1:
		<tr>
				<td>{{rows_1[r][0]}}</td>
				<td>{{r}}</td>
				<td>{{rows_1[r][1]}}</td>
		</tr>
	%end
</table>




<table border="2" style="float: left;">
	<tr>
			<th>Félag </th><th>Stöð</th><th>Verð á dísel</th>
	</tr>
	

			%for r in rows_2:
				<tr>
				<td>{{rows_2[r][0]}}</td>
				<td>{{r}}</td>
				<td>{{rows_2[r][1]}}</td>
				</tr>	
			%end
			
	</table>

</html>