#!/usr/bin/env python3
"""Exercise all bundled helper CLIs with isolated synthetic fixtures."""
from pathlib import Path
import json, subprocess, tempfile, sys
root=Path(__file__).resolve().parents[1]; skills=root/'skills'
with tempfile.TemporaryDirectory(prefix='product-helpers-') as tmp:
 w=Path(tmp)
 (w/'events.csv').write_text('user_id,cohort_date,activity_date\na,2026-01-01,2026-01-01\na,2026-01-01,2026-01-02\nb,2026-01-01,2026-01-01\n')
 (w/'funnel.csv').write_text('user_id,stage\na,visit\na,signup\nb,visit\n')
 (w/'interview.txt').write_text('I spend two hours each week exporting reports. I struggle with manual data entry and need a simpler export workflow.')
 (w/'citations.txt').write_text('See  and doi:10.1234/example for evidence.')
 (w/'competitors.json').write_text(json.dumps({'competitors':[{'name':'A','scores':{'ux':8,'pricing':6}},{'name':'B','scores':{'ux':5,'pricing':9}}]}))
 (w/'landing.json').write_text(json.dumps({'name':'Example','hero':{'headline':'Review evidence clearly','subheadline':'A product research workspace.'}}))
 (w/'saas.json').write_text(json.dumps({'name':'example-app','stack':'nextjs','description':'Example only'}))
 project=w/'project';project.mkdir();(project/'README.md').write_text('# Example\nLocal fixture.\n');(project/'.gitignore').write_text('node_modules/\n.env\n');(project/'package.json').write_text('{"name":"example","scripts":{"test":"node test.js"}}');(project/'app.test.js').write_text('require("node:assert").strictEqual(1+1,2);\n')
 cases=[
 ('agile-product-owner','user_story_generator.py',['--sample']),
 ('apple-hig-expert','hig_checker.py',['contrast','#000000','#FFFFFF']),
 ('code-to-prd','codebase_analyzer.py',[str(project),'-o',str(w/'analysis.json')]),
 ('code-to-prd','prd_scaffolder.py',[str(skills/'code-to-prd/assets/sample-analysis.json'),'-o',str(w/'prd')]),
 ('competitive-teardown','competitive_matrix_builder.py',[str(w/'competitors.json'),'--format','json']),
 ('experiment-designer','sample_size_calculator.py',['--baseline-rate','0.12','--mde','0.02','--mde-type','absolute']),
 ('landing-page-generator','landing_page_scaffolder.py',[str(w/'landing.json'),'--format','html','--output',str(w/'landing.html')]),
 ('product-analytics','metrics_calculator.py',['retention',str(w/'events.csv'),'--max-period','1','--format','json']),
 ('product-analytics','metrics_calculator.py',['cohort',str(w/'events.csv'),'--max-period','1','--format','json']),
 ('product-analytics','metrics_calculator.py',['funnel',str(w/'funnel.csv'),'--stages','visit,signup','--format','json']),
 ('product-discovery','assumption_mapper.py',['--assumption','Users need exports|desirability|0.9|0.2']),
 ('product-manager-toolkit','customer_interview_analyzer.py',[str(w/'interview.txt'),'--json']),
 ('product-manager-toolkit','rice_prioritizer.py',[str(skills/'product-manager-toolkit/assets/rice_input_template.csv'),'--output','json']),
 ('product-skills','discovery_cadence_tracker.py',['--sample']),
 ('product-skills','ost_linter.py',['--sample']),
 ('product-skills','product_goal_router.py',['--sample']),
 ('product-strategist','okr_cascade_generator.py',['growth','--json']),
 ('research-summarizer','extract_citations.py',[str(w/'citations.txt'),'--output','json']),
 ('research-summarizer','format_summary.py',['--template','academic','--output','json']),
 ('roadmap-communicator','changelog_generator.py',['--demo']),
 ('saas-scaffolder','project_bootstrapper.py',[str(w/'saas.json'),'--output-dir',str(w/'saas'),'--format','json']),
 ('spec-to-repo','validate_project.py',[str(project),'--format','json']),
 ('ui-design-system','design_token_generator.py',['#3366CC','--style','modern','--format','json']),
 ('ux-researcher-designer','persona_generator.py',['--sample','--output','json']),
 ]
 failures=[]
 for skill,script,args in cases:
  r=subprocess.run([sys.executable,str(skills/skill/'scripts'/script),*args],cwd=w,text=True,capture_output=True,timeout=30)
  if r.returncode: failures.append((script,r.returncode,r.stderr[-1000:],r.stdout[-600:]))
  else:
   if script=='metrics_calculator.py' and args[0]=='retention':
    data=json.loads(r.stdout); assert data['base_users']==2 and data['periods'][1]['retention_rate']==0.5
   if script=='metrics_calculator.py' and args[0]=='funnel': assert json.loads(r.stdout)['stages'][1]['conversion_from_first']==0.5
 print(json.dumps({'scenarios':len(cases),'unique_helpers':len({x[1] for x in cases}),'failures':failures},indent=2))
 assert not failures
 assert (w/'prd').is_dir() and (w/'landing.html').exists() and (w/'saas/package.json').exists()
