/* Pure data comparison. Ambiguous keys never silently overwrite one another. */
function reconcile(before,after){
 const index=rows=>{if(!Array.isArray(rows)||rows.length>10000)throw Error('Нужен массив, максимум 10 000 строк.');const m=new Map();for(const row of rows){if(!row||typeof row!=='object'||typeof row.sku!=='string'||!row.sku.trim())throw Error('У каждой строки должен быть непустой текстовый sku.');const k=row.sku.trim();if(!m.has(k))m.set(k,[]);m.get(k).push(row);}return m;};
 const a=index(before),b=index(after),out=[];const valid=r=>typeof r.price==='number'&&Number.isFinite(r.price)&&r.price>=0;
 for(const sku of new Set([...a.keys(),...b.keys()])){const x=a.get(sku)||[],y=b.get(sku)||[];let status;if(x.length>1||y.length>1)status='Дубль — проверить';else if([...x,...y].some(r=>!valid(r)))status='Цена — проверить';else if(!x.length)status='Добавлен';else if(!y.length)status='Удалён';else if(x[0].price!==y[0].price)status='Цена изменилась';else if(x[0].name!==y[0].name)status='Название изменилось';else status='Без изменений';out.push({sku,status,before:x.map(r=>r.price),after:y.map(r=>r.price)});}return out;
}
function receive(rows,item){if(rows.some(x=>x.id===item.id))return false;rows.push({...item});return true;}
if(typeof module!=='undefined')module.exports={reconcile,receive};
