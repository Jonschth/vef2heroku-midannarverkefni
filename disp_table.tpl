<link  type="text/css" href="/static/tafla_f.css" rel="stylesheet">
<h1> Yfirlit yfir söluaðila </h1>
<p> Dagsetning uppfærslu {{!dagsetning}} </p>


<table>
	<tr>
		<th>
			Söluaðilar
		</th>
	</tr>

	%for company in sa:
		<tr>
			<td>
				{{company}}
			</td>
		</tr>
	%end

</table>
	

<h1>
	Ódírasta bensínið og díselið er:
</h1>
	<table>
		<tr>
			%for r in besta:
			<tr>
					<td>{{besta[r][0]}}</td>
					<td>{{r}}</td>
					<td>{{besta[r][1]}}</td>
			</tr>
			%end
		</tr>
	</table>

</h1>



</html>