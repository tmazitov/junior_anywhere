import { IconifyIconSize } from "@iconify/vue/dist/iconify.js"

interface Icon {
	name:		string	
	height?:	IconifyIconSize 
	width?:		IconifyIconSize
	color?:		string	
	onClick?: 	Function
	isHidden?:	Boolean
}

export default Icon