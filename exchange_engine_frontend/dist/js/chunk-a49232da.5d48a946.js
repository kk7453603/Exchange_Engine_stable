(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-a49232da"],{"3f18":function(t,e,i){"use strict";i.r(e);var n=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-row",{staticClass:"grey lighten-5 align-stretch",attrs:{"no-gutters":""}},[i("v-col",[i("v-list",{attrs:{"two-line":"",subheader:""}},[i("v-list-item-group",{attrs:{color:"primary"}},t._l(t.stocks,(function(e,n){return i("div",{key:e.id,on:{click:function(i){return t.selectStock(e.id)}}},[i("v-list-item",[i("v-list-item-avatar",{staticClass:"justify-center",attrs:{size:"25px",color:"primary"}},[i("span",{staticClass:"white--text"},[t._v(" "+t._s(e.name[0]+e.name[1])+" ")])]),i("v-list-item-content",[i("v-list-item-title",{domProps:{textContent:t._s(e.name)}}),i("v-list-item-subtitle",{domProps:{textContent:t._s(e.description)}})],1),i("v-list-item-action",[i("v-list-item-title",[t._v(" "+t._s(e.price.toFixed(2))+"₮ ")])],1),i("v-list-item-action",[e.is_active?i("v-icon",{attrs:{color:"green"}},[t._v(" mdi-circle ")]):i("v-icon",{attrs:{color:"red"}},[t._v(" mdi-circle ")])],1)],1),n<t.stocks.length-1?i("v-divider",{key:"divider-"+n}):t._e()],1)})),0)],1)],1),i("v-divider",{attrs:{vertical:""}}),i("v-col",[void 0!=t.selectedStonkID?i("v-card",{staticClass:"pa-6",attrs:{elevation:"0",tile:""}},[i("v-card-title",{domProps:{textContent:t._s(t.selectedStock.name)}}),i("v-card-subtitle",[t._v(" Текущая цена: "+t._s(t.selectedStock.price.toFixed(2))+"₮ ")]),i("v-card-text",[t._v(t._s(t.selectedStock.description))]),i("v-container",[i("v-btn-toggle",{attrs:{mandatory:""},model:{value:t.selectedCandlesType,callback:function(e){t.selectedCandlesType=e},expression:"selectedCandlesType"}},[i("v-btn",[t._v(" 1MIN ")]),i("v-btn",[t._v(" 5MIN ")]),i("v-btn",[t._v(" 15MIN ")]),i("v-btn",[t._v(" 30MIN ")]),i("v-btn",[t._v(" 60MIN ")])],1),i("apexchart",{attrs:{type:"candlestick",options:t.options,series:t.series}})],1),i("v-form",[i("v-text-field",{attrs:{hint:"",label:"Количество",type:"number"},model:{value:t.amount,callback:function(e){t.amount=e},expression:"amount"}}),i("v-checkbox",{staticClass:"shrink mr-2 mt-0",attrs:{"hide-details":"",label:"Отложенная заявка"},model:{value:t.limit_order,callback:function(e){t.limit_order=e},expression:"limit_order"}}),t.limit_order?i("v-text-field",{attrs:{"append-icon":"mdi-currency-mnt",disabled:!t.limit_order,hint:"",label:"Цена",type:"number"},model:{value:t.price,callback:function(e){t.price=e},expression:"price"}}):t._e(),i("v-checkbox",{staticClass:"shrink mr-2 mt-0",attrs:{"hide-details":"",label:"Торговля с плечом",disabled:t.limit_order},model:{value:t.leverage_trade,callback:function(e){t.leverage_trade=e},expression:"leverage_trade"}}),t.leverage_trade?i("v-text-field",{attrs:{hint:"",label:"Размер плеча",type:"number"},model:{value:t.ratio,callback:function(e){t.ratio=e},expression:"ratio"}}):t._e(),i("v-card-actions",[i("v-btn",{attrs:{color:"success"},on:{click:function(e){return t.trade(0)}}},[t._v(" Купить ")]),i("v-btn",{attrs:{color:"error"},on:{click:function(e){return t.trade(1)}}},[t._v(" Продать ")])],1)],1)],1):i("v-container",[i("BaseTitle",{attrs:{align:"center",weight:"regular"}},[t._v(" Ни одной акции не выбрано ")]),i("BaseBody",{staticClass:"text-center"},[t._v(" Пожалуйста, выберите любую акцию из списка слева для просмотра ее информации ")])],1)],1)],1)},a=[],s=(i("d81d"),i("b680"),i("d3b7"),i("25f0"),i("b0c0"),i("7db0"),i("cb98")),o={name:"App",data:function(){return{selectedCandlesType:0,selectedStonkID:void 0,limit_order:!1,leverage_trade:!1,price:0,amount:1,stocks:[],ratio:0,item:"",stocksInterval:void 0,options:{chart:{id:"main-chart",locales:[{name:"ru",options:{months:["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"],shortMonths:["Янв","Фев","Мар","Апр","Май","Июн","Июл","Авг","Сен","Окт","Ноя","Дек"],days:["Воскресенье","Понедельник","Вторник","Среда","Четверг","Пятница","Суббота"],shortDays:["Вс","Пн","Вт","Ср","Чт","Пт","Сб"],toolbar:{exportToSVG:"Скачать SVG",exportToPNG:"Скачать PNG",menu:"Меню",selection:"Зона",selectionZoom:"Зона увелечения",zoomIn:"Увеличить",zoomOut:"Уменьшить",pan:"Переместить",reset:"Домой"}}}],defaultLocale:"ru",animations:{enabled:!0,easing:"easeinout",speed:300,animateGradually:{enabled:!0,delay:100},dynamicAnimation:{enabled:!0,speed:100}},toolbar:{show:!0,offsetX:0,offsetY:0,tools:{download:!0,selection:!0,zoom:!0,zoomin:!0,zoomout:!0,pan:!0,reset:1,customIcons:[]}}},xaxis:{type:"datetime"},yaxis:{tooltip:{enabled:!0}}},series:[{data:[]}]}},watch:{selectedCandlesType:function(){this.getCandles()}},methods:{getStocks:function(){var t=this;s["a"].get("api/v1/stocks/",{headers:{Authorization:"Bearer ".concat(this.$store.getters.accessToken)}}).then((function(e){t.stocks=e.data})).catch((function(e){console.log(e),clearInterval(t.stocksInterval)}))},getCandles:function(){var t=this;s["a"].get("http://140.238.223.202/api/v1/candles/"+this.selectedStonkID+"/"+(this.selectedCandlesType+1)).then((function(e){var i=e.data.map((function(t){return[Date.parse(t.date),[t.open,t.high,t.low,t.close].map((function(t){return t.toFixed(2)}))]}));t.candlesInterval=setInterval(function(){this.getCandles()}.bind(t),6e4),t.series=[{data:i}]})).catch((function(t){console.log(t)}))},trade:function(t){var e=this,i=this.leverage_trade&&!this.leverage_trade?"trading/leverage/":"orders/add";s["a"].post(i,{stock:this.selectedStock.name.toString(),type:t,price:this.limit_order?this.price:0,amount:this.amount,ratio:this.ratio},{headers:{Authorization:"Bearer ".concat(this.$store.getters.accessToken)}}).then((function(t){console.log(t),e.$store.commit({type:"showSnackbar",text:"Вы создали заявку"})})).catch((function(t){console.log(t),e.$store.commit({type:"showSnackbar",text:"Введите корректные данные для торговли"})}))},selectStock:function(t){this.selectedStonkID=t,this.getCandles()}},computed:{generateAlert:function(){var t="Вы хотите создать ";return t+=this.limit_order?"отложенную заявку по цене "+this.price:"заявку по текущей цене ",t+=this.leverage_trade?"с плечом  ":"",t},selectedStock:function(){var t=this;return this.stocks.find((function(e){return e.id===t.selectedStonkID}))}},mounted:function(){this.getStocks(),this.stocksInterval=setInterval(function(){this.getStocks()}.bind(this),5e3)},destroyed:function(){clearInterval(this.stocksInterval)}},r=o,l=i("2877"),c=i("6544"),d=i.n(c),u=i("8336"),h=i("5530"),p=(i("7e58"),i("604c")),v=p["a"].extend({name:"button-group",provide:function(){return{btnToggle:this}},computed:{classes:function(){return p["a"].options.computed.classes.call(this)}},methods:{genData:p["a"].options.methods.genData}}),m=i("a9ad"),f=i("58df"),b=Object(f["a"])(v,m["a"]).extend({name:"v-btn-toggle",props:{backgroundColor:String,borderless:Boolean,dense:Boolean,group:Boolean,rounded:Boolean,shaped:Boolean,tile:Boolean},computed:{classes:function(){return Object(h["a"])(Object(h["a"])({},v.options.computed.classes.call(this)),{},{"v-btn-toggle":!0,"v-btn-toggle--borderless":this.borderless,"v-btn-toggle--dense":this.dense,"v-btn-toggle--group":this.group,"v-btn-toggle--rounded":this.rounded,"v-btn-toggle--shaped":this.shaped,"v-btn-toggle--tile":this.tile},this.themeClasses)}},methods:{genData:function(){var t=this.setTextColor(this.color,Object(h["a"])({},v.options.methods.genData.call(this)));return this.group?t:this.setBackgroundColor(this.backgroundColor,t)}}}),g=i("b0af"),k=i("99d9"),C=(i("6ca7"),i("ec29"),i("9d26")),x=i("c37a"),I=(i("4de4"),i("5607")),y=i("2b0e"),_=y["a"].extend({name:"rippleable",directives:{ripple:I["a"]},props:{ripple:{type:[Boolean,Object],default:!0}},methods:{genRipple:function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{};return this.ripple?(t.staticClass="v-input--selection-controls__ripple",t.directives=t.directives||[],t.directives.push({name:"ripple",value:{center:!0}}),this.$createElement("div",t)):null}}}),V=i("80d2"),S=y["a"].extend({name:"comparable",props:{valueComparator:{type:Function,default:V["h"]}}});function w(t){t.preventDefault()}var A=Object(f["a"])(x["a"],_,S).extend({name:"selectable",model:{prop:"inputValue",event:"change"},props:{id:String,inputValue:null,falseValue:null,trueValue:null,multiple:{type:Boolean,default:null},label:String},data:function(){return{hasColor:this.inputValue,lazyValue:this.inputValue}},computed:{computedColor:function(){if(this.isActive)return this.color?this.color:this.isDark&&!this.appIsDark?"white":"primary"},isMultiple:function(){return!0===this.multiple||null===this.multiple&&Array.isArray(this.internalValue)},isActive:function(){var t=this,e=this.value,i=this.internalValue;return this.isMultiple?!!Array.isArray(i)&&i.some((function(i){return t.valueComparator(i,e)})):void 0===this.trueValue||void 0===this.falseValue?e?this.valueComparator(e,i):Boolean(i):this.valueComparator(i,this.trueValue)},isDirty:function(){return this.isActive},rippleState:function(){return this.isDisabled||this.validationState?this.validationState:void 0}},watch:{inputValue:function(t){this.lazyValue=t,this.hasColor=t}},methods:{genLabel:function(){var t=x["a"].options.methods.genLabel.call(this);return t?(t.data.on={click:w},t):t},genInput:function(t,e){return this.$createElement("input",{attrs:Object.assign({"aria-checked":this.isActive.toString(),disabled:this.isDisabled,id:this.computedId,role:t,type:t},e),domProps:{value:this.value,checked:this.isActive},on:{blur:this.onBlur,change:this.onChange,focus:this.onFocus,keydown:this.onKeydown,click:w},ref:"input"})},onBlur:function(){this.isFocused=!1},onClick:function(t){this.onChange(),this.$emit("click",t)},onChange:function(){var t=this;if(this.isInteractive){var e=this.value,i=this.internalValue;if(this.isMultiple){Array.isArray(i)||(i=[]);var n=i.length;i=i.filter((function(i){return!t.valueComparator(i,e)})),i.length===n&&i.push(e)}else i=void 0!==this.trueValue&&void 0!==this.falseValue?this.valueComparator(i,this.trueValue)?this.falseValue:this.trueValue:e?this.valueComparator(i,e)?null:e:!i;this.validate(!0,i),this.internalValue=i,this.hasColor=i}},onFocus:function(){this.isFocused=!0},onKeydown:function(t){}}}),T=A.extend({name:"v-checkbox",props:{indeterminate:Boolean,indeterminateIcon:{type:String,default:"$checkboxIndeterminate"},offIcon:{type:String,default:"$checkboxOff"},onIcon:{type:String,default:"$checkboxOn"}},data:function(){return{inputIndeterminate:this.indeterminate}},computed:{classes:function(){return Object(h["a"])(Object(h["a"])({},x["a"].options.computed.classes.call(this)),{},{"v-input--selection-controls":!0,"v-input--checkbox":!0,"v-input--indeterminate":this.inputIndeterminate})},computedIcon:function(){return this.inputIndeterminate?this.indeterminateIcon:this.isActive?this.onIcon:this.offIcon},validationState:function(){if(!this.isDisabled||this.inputIndeterminate)return this.hasError&&this.shouldValidate?"error":this.hasSuccess?"success":null!==this.hasColor?this.computedColor:void 0}},watch:{indeterminate:function(t){var e=this;this.$nextTick((function(){return e.inputIndeterminate=t}))},inputIndeterminate:function(t){this.$emit("update:indeterminate",t)},isActive:function(){this.indeterminate&&(this.inputIndeterminate=!1)}},methods:{genCheckbox:function(){return this.$createElement("div",{staticClass:"v-input--selection-controls__input"},[this.$createElement(C["a"],this.setTextColor(this.validationState,{props:{dense:this.dense,dark:this.dark,light:this.light}}),this.computedIcon),this.genInput("checkbox",Object(h["a"])(Object(h["a"])({},this.attrs$),{},{"aria-checked":this.inputIndeterminate?"mixed":this.isActive.toString()})),this.genRipple(this.setTextColor(this.rippleState))])},genDefaultSlot:function(){return[this.genCheckbox(),this.genLabel()]}}}),B=i("62ad"),D=i("a523"),$=i("ce7e"),O=i("4bd4"),j=i("132d"),L=i("8860"),z=i("da13"),F=i("1800"),M=i("8270"),N=i("5d23"),E=i("1baa"),G=i("0fd9"),P=i("8654"),R=Object(l["a"])(r,n,a,!1,null,null,null);e["default"]=R.exports;d()(R,{VBtn:u["a"],VBtnToggle:b,VCard:g["a"],VCardActions:k["a"],VCardSubtitle:k["b"],VCardText:k["c"],VCardTitle:k["d"],VCheckbox:T,VCol:B["a"],VContainer:D["a"],VDivider:$["a"],VForm:O["a"],VIcon:j["a"],VList:L["a"],VListItem:z["a"],VListItemAction:F["a"],VListItemAvatar:M["a"],VListItemContent:N["a"],VListItemGroup:E["a"],VListItemSubtitle:N["b"],VListItemTitle:N["c"],VRow:G["a"],VTextField:P["a"]})},"6ca7":function(t,e,i){},"7e58":function(t,e,i){},ec29:function(t,e,i){}}]);
//# sourceMappingURL=chunk-a49232da.5d48a946.js.map