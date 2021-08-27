select
md5(concat(cast(nvl(activityid, '') as string), cast(nvl(productid, '') as string), nvl(sku, ''), nvl(spusn, ''))) `_id`
,productname
,firstlevelcategoryname
,secondlevelcategoryname
,windowname
,areaid
,skustatus
,saletime
,tmshowstart
,tmshowend
,'TRUE' haswindow
,saleqty
,vendorid
,nextdaypickup
,limitqty
,activityid
,saleamt
,tmbuyend
,sku
,productid
,spusn
,marketamt
,userlimitqty
,primaryurls
,videourl
,shelflife
,producttype
,tmbuystart
,assigntype
,verificationcode
,preproductid
,tmpickup
from dw_search.daily_sale_product_info
where dt = '${dt}'